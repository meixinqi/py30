import json
import re
resp = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 200713,
        "leave_amount": 4000.0,
        "mobile_phone": "18605671115",
        "reg_name": "美丽可爱的小简",
        "reg_time": "2020-06-29 11:52:20.0",
        "type": 1,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2020-07-06 21:48:53",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIwMDcxMywiZXhwIjoxNTk0MDQzMzMzfQ.WJMI0-t7YZD8FtAiaYR8-SH1p58_7fJjnvS6xVw7_hYTe7eVIyxj3W2Oj7SlwR8dDZBc1T59U2ngRROXyFjx_Q"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
}
resp=json.dumps(resp)
result=re.findall('"token":(.*?)}',resp)
print(result)
s='****qwqew23232'
ss=re.findall('\W+',s)
print(ss)
sear=re.search('token',resp)
print(sear)