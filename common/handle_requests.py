import requests
# def __headers(token=None):
#     headers = {"X-Lemonban-Media-Type": "lemonban.v2",
#               "Content-Type": "application/json"}
#     if token:
#         headers['Authorization']='Bearer '+token
#     return headers
# def send_requests(method,url,data=None,token=None):
#     headers=__headers(token)
#     method=method.upper()
#     if method=='GET':
#         resp=requests.get(url,data,headers=headers)
#         return resp
#     elif method=='POST':
#         resp=requests.post(url,json=data,headers=headers)
#         return resp
# if __name__ == '__main__':
#     login_url = "http://8.129.91.152:8766/futureloan/member/register"
#     login_datas = {"mobile_phone":18813167786, "pwd":"1234567890"}
#     resp = send_requests("POST",login_url,login_datas)
#     # token = resp.json()["data"]["token_info"]["token"]
#     #
#     # recharge_url = "http://8.129.91.152:8766/futureloan/member/register"
#     # recharge_data = {"member_id": 200119, "amount": 2000}
#     # resp = send_requests("POST",recharge_url,recharge_data,token)
#     print(resp.json())
"""
======================
Author: 柠檬班-小简
Time: 2020/6/29 21:12
Project: py30-接口自动化
Company: 湖南零檬信息技术有限公司
======================
"""
"""
基于项目做定制化封装
1、鉴权:token
2、项目通用的请求头:
    {"X-Lemonban-Media-Type": "lemonban.v2"}

3、请求体格式：application/json
"""
import requests
from common.logger import logger
from common.handle_ini import conf

def send_requests(method, url, data=None, token=None):
    """

    :param method:
    :param url:
    :param data:字典形式的数据。
    :param token:
    :return:
    """
    logger.info("发起一次HTTP请求")
    # 得到请求头
    headers = __handle_header(token)
    #得到完整的url---拼接url
    url=__pre_url(url)
    #请求数据的处理，如果数据是字符串，则转换成字典对象
    data=__pre_data(data)
    logger.info("请求头为：{}".format(headers))
    logger.info("请求方法为：{}".format(method))
    logger.info("请求url为：{}".format(url))
    logger.info("请求数据为：{}".format(data))
    # 根据请求类型，调用请求方法
    method = method.upper()  # 大写处理
    if method == "GET":
        resp = requests.get(url, data, headers=headers)
    else:
        resp = requests.post(url, json=data, headers=headers)
    logger.info("响应状态码为：{}".format(resp.status_code))
    logger.info("响应数据为：{}".format(resp.json()))
    return resp

def __handle_header(token=None):
    """
    处理请求头。加上项目当中必带的请求头。如果有token，加上token。
    :param token: token值
    :return: 处理之后headers字典
    """
    headers = {"X-Lemonban-Media-Type": "lemonban.v2",
               "Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers

def __pre_url(url):
    base_url=conf.get("serve","base_url")
    if url.startswith("/"):
        url=base_url+url
    else:
        url=base_url+"/"+url
    return url

def __pre_data(data):
    """
    如果数据是字符串，则转换成字典
    :param data:测试用例数据
    :return:处理后的数据，字典对象
    """
    if data is not  None and isinstance(data,str):
        if data.find("null")!=-1:
            data=data.replace("null","None")
        else:
            data=eval(data)
    return data

if __name__ == '__main__':
    #login_url = "http://api.lemonban.com/futureloan/member/login"
    login_datas = {"mobile_phone":13845467789, "pwd": "1234567890"}
    #resp = send_requests("POST", "/member/login", login_datas)
    #print(resp)
    print(__pre_url("member/register"))



