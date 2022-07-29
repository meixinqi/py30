import json
import os.path
import sys
import unittest
from ddt import ddt,data
from common.handle_requests import send_requests
from common.handle_ini import conf
from common.handle_path import case_dir
from common.handle_xlsx import Handle_xlsx
from common.logger import logger
from BeautifulReport import BeautifulReport

file_path=os.path.join(case_dir,'api_cases.xlsx')
datas=Handle_xlsx(file_path,'登录')
login_datas=datas.read_xlsx()
datas.close_file()

@ddt
class TestLogin(unittest.TestCase):

    @data(*login_datas)
    def test_ogin(self,case):
        case["request"]=json.loads(case["request"])
        base_url = conf.get('serve', 'base_url')
        url = os.path.join(base_url, '/member/login')
        print(url)
        expected=eval(case["expected"])
        resp=send_requests('post',url=url,data=case["request"])
        logger.info("***********响应数据*********",resp.json())
        try:
            self.assertEqual(resp.json()["code"],expected["code"])
            self.assertEqual(resp.json()["msg"], expected["msg"])

        except AssertionError:
            print("*********FAIL************")
        else:
            print("*********success**********")
if __name__ == '__main__':
    #创建测试套件
    suite=unittest.TestSuite()
    #将用例添加到套件中
    suite.addTest(TestLogin("test_login"))
    #创建测试用例执行程序
    runner=unittest.TextTestRunner()
    runner.run(suite)
    unittest.main