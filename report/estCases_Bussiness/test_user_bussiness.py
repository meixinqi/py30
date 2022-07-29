import os.path
import unittest
from ddt import ddt,data
from common.handle_data import Env_data
from common.handle_data import clear_Env_data_attrs
from common.handle_phone import generator_new_phone
from common.handle_xlsx import Handle_xlsx
from common.handle_path import base_dir
from common.handle_data import replace_mark_with_regular
from common.handle_requests import send_requests
from common.handle_extract_data_from_resp import exract_data_from_resp

file_path=os.path.join(base_dir,'aps_cases.xlsx')
datas=Handle_xlsx(file_path,'业务流')
bussinesss_datas=datas.read_xlsx()


@ddt
class Test_user_bussiness(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        clear_Env_data_attrs()
        #生成一个新的手机号
        new_phone=generator_new_phone()
        setattr(Env_data,"phone",new_phone)

    @data(*business_datas)
    def test_user_bussiness(self,case):
        replace_mark_with_regular(case)
        if hasattr(Env_data,token):
            resp=send_requests(case["method"],url,data=case["request"],token=Env_data.token)
        else:
            resp=send_requests(case["method"],url,data=case["request"])
        if case["extract_data"]:
            exract_data_from_resp(case["extract_data"],resp.json())


