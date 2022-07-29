import json
import unittest
import os
import time

import requests
from ddt import ddt,data
from common.logger import logger
from common.handle_yml import yml_data
from common.handle_path import case_dir,report_dir,cases_dir
from common.handle_xlsx import Handle_xlsx
from common.handle_requests import send_requests
from common.handle_ini import conf
from common.handle_data import replace_mark_with_data
from common.handle_phone import generator_new_phone
#file_path=os.path.join(case_url,'login.yml')
#login_data=yml_data.read_yml(file_path)

case_path=os.path.join(case_dir,'api_cases.xlsx')
datas=Handle_xlsx(case_path,'注册')
register_datas=datas.read_xlsx()
datas.close_file()#记得关闭文件啊

@ddt
class TestDemo(unittest.TestCase):

    @data(*register_datas)
    def test_register(self,case):
        if case["request"].find("#pone#")!=-1:
            new_phone=generator_new_phone()
            case=replace_mark_with_data(case,"#phone#",new_phone)
        # base_url=conf.get('serve','base_url')
        # url=os.path.join(base_url,case['url'])
        header = {"X-Lemonban-Media-Type": "lemonban.v2",
                   "Content-Type": "application/json"}
        url='http://8.129.91.152:8766/futureloan/member/login'
        expected=json.loads(case['expected'])
        logger.info('title是{}，测试数据：{}，预期结果是：{}'.format(case['title'],case['request'],expected))
        #resp=requests.post(url,json=case['request'],headers=header)#json可以，data报错？case['request']是字典形式的数据，在handle_xlsx中已处理
        resp=send_requests('post',url=url,data=case['request'])
        print(resp.text)
        try:
            self.assertEqual(resp.json()['code'],expected['code'])
        except AssertionError:
            print('****断言失败*****')
            raise
        else:
            print('***********测试用例执行通过***************')

# if __name__ == '__main__':
#     #构建测试集合
#     suit=unittest.TestSuite()
#     #suit.addTest(TestDemo('test_isUpper'))
#     #suit.addTest(TestDemo2('test_upper'))
#     suit.addTest(TestDemo('test_login'))
#     # suit1=unittest.TestLoader.loadTestsFromTestCase(TestDemo)
#     # suit2=unittest.TestLoader.loadTestsFromTestCase(TestDemo2)
#     # suit=unittest.TestSuite([suit1,suit2])
#     #执行集合
#     # runner=unittest.TextTestRunner()
#     # runner.run(suit)
#     # from BeautifulReport import BeautifulReport
#     discover = unittest.TestLoader().discover(cases_dir, pattern='test*.py')
#     # br = BeautifulReport(discover)
#     # br.report('单元测试框架unittest的报告',report_url, "{}.html".format(time.strftime("%y%m%d")))
#     from HTMLTestRunner import HTMLTestRunner
#     with open("report3.html",'wb')as fs:
#         runner=HTMLTestRunner(fs,title='第一个htmlrunner')
#         runner.run(suit)
