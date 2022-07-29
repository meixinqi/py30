#随机生成手机号，替换excel测试用例
import random
from faker import Faker
from common.Handle_db import db
from common.handle_ini import conf
from common.handle_requests import send_requests

def generator_new_phone():
    phone=__generate_phone()
    while True:
        # 去数据库查询是否已存在，若存在，重新生成
        count=db.count_data('select * from member where mobile_phone="{}"'.format(phone))
        if count==0:
            db.db_close()
            return phone

def __generate_phone():
    fake=Faker("zh-CN")
    phone=str(fake.phonenumber_prefix())
    for _ in  range(8):
        phone+=str(random.randint(0,9))
    return phone

def get_old_phone():
    user=conf.get("mobile_uesr","mobile_phone")
    pwd=conf.get("mobile_uesr","pwd")
    send_requests("post","member/register",data={"mobile_phone":user,"pwd":pwd})
    return user,pwd

if __name__ == '__main__':
    print(generator_new_phone())
    print(get_old_phone())
