from jsonpath import jsonpath
from common.logger import logger
from common.handle_data import Env_data


def exract_data_from_resp(extract_exprs,resp_dict):
    #将提取的字符串表达式转换成字典对象
    extract_exprs=eval(extract_exprs)
    for key,value in extract_exprs.items():
        #在返回值中匹配value值
        res=str(jsonpath(resp_dict,value)[0])
        #设置环境变量
        logger.info("设置环境变量 key:{},value:{}".format(key,res))
        #将匹配到的值设置为环境变量
        setattr(Env_data,key,res)

if __name__ == '__main__':
    ss = '{"member_id":"$..id","token":"$..token"}'
    response = {'code': 0, 'msg': 'OK',
                'data': {'id': 200713, 'leave_amount': 8555405.44, 'mobile_phone': '18605671115',
                         'reg_name': '美丽可爱的小简', 'reg_time': '2020-06-29 11:52:20.0', 'type': 1,
                         'token_info': {'token_type': 'Bearer', 'expires_in': '2020-07-08 21:33:05',
                                        'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIwMDcxMywiZXhwIjoxNTk0MjE1MTg1fQ.9oTx_KSOwjEg4V9Ez_P6QV-3aBk3QCCFRZk3OlTnGDElkVanMLFK_H5wgI_9xolnjBNZE9TMI7e1nSOPKWj2HA'}},
                'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
    exract_data_from_resp(ss,response)
    print(Env_data.__dict__)


