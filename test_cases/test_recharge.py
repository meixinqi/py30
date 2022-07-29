import json
import unittest
import os
from jsonpath import jsonpath
from ddt import ddt,data
from common.handle_requests import send_requests
from common.handle_ini import conf
from common.handle_path import case_dir
from common.handle_xlsx import Handle_xlsx
from common.handle_data import replace_mark_with_data,Env_data#环境变量类
from common.Handle_db import db
from common.logger import logger


file_path=os.path.join(case_dir,'api_cases.xlsx')
datas=Handle_xlsx(file_path,"充值")
recharge_datas=datas.read_xlsx()
datas.close_file()

@ddt
class TestRecharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        login_url=os.path.join(conf.get('serve','base_url'),'member/login')
        data={"mobile_phone":conf.get('login_user',"mobile_phone"),
              "pwd":conf.get("login_user","pwd")
              }
        login_resp=send_requests('post',url=login_url,data=data)
        # 设置类属性保存token,
        #cls.token=login_resp.json()["data"]["token_info"]["token"]
        #cls.token=jsonpath(login_resp.json(),"$..token")[0]
        #如果是登录与充值之间得接口则不好用这种类属性，此时可以创建环境变量得方式，类似于postman中得环境变量，在每个接口中都是可以调用
        setattr(Env_data,"token",jsonpath(login_resp.json(),"$..token")[0])#返回的是列表，用索引获取值，存放匹配到的所有值
        setattr(Env_data,"member_id",jsonpath(login_resp.json(),"$..id")[0])

    @data(*recharge_datas)
    def test_recharge(self,case):
        login_url = os.path.join(conf.get('serve', 'base_url'), case["url"])
        if case["request"].find("#member_id#")!=-1:
            case=replace_mark_with_data(case,"#member_id#",str(Env_data.member_id))
        case["request"] = json.loads(case["request"])
        if case["check_sql"] is not None:
            before_leave_amount=db.select_one_data(case["check_sql"])['leave_amount']
            #print(type(before_leave_amount))  Decimal
            #如果不替换excel中的expected里的amount，直接用after_leave_amount直接和响应数据进行比对是正确的,sql:SELECT * from member where id=23605
            after_leave_amount = round(float(before_leave_amount) +case["request"]["amount"],2)
            #如果需要替换，则会报错，因为数据库里的格式是decimal，所以此处要转换成str，解决方法在sql语句中用CAST进行转换
            case=replace_mark_with_data(case,"#money#",str(after_leave_amount))
        resp = send_requests('post', url=login_url, data=case["request"],token=Env_data.token)
        expected=json.loads(case["expected"])
        try:
            self.assertEqual(expected["code"],resp.json()["code"])
            self.assertEqual(expected["msg"],resp.json()["msg"])
            if case["check_sql"]:
                self.assertEqual(resp.json()["data"]["id"],expected["data"]["id"])
                #校验响应数据
                #如果不替换excel中的expected里的amount，直接用after_leave_amount直接和响应数据进行比对是正确的
                self.assertEqual(resp.json()["data"]["leave_amount"],expected["data"]["leave_amount"])

                #校验数据库
                user_money_after_recharge = db.select_one_data(case["check_sql"])["leave_amount"]
                self.assertEqual("{:.2f}".format(resp.json()["data"]["leave_amount"]),"{:.2f}".format(float(user_money_after_recharge)))
        except AssertionError:
            logger.info("断言失败")
            raise
        else:
            print("用例执行通过")
