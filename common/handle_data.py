
#设置环境变量
import re
from  common.handle_ini import conf


class Env_data:
    pass

def clear_Env_data_attrs():
    values=dict(Env_data.__dict__.items())
    for key,value in values:
        if  key.startswith("__"):
            pass
        else:
            delattr(Env_data,key)
#使用正则表达式替换excel中的mark标识
def replace_mark_with_regular(case):
    for key,value in case.items():
        if value is not  None and isinstance(value,str):
            case[key]=replace_by_regular(value)
    return case

def replace_by_regular(data):
    res=re.findall("#(.*?)#",data)
    if res:
        for item in res:
            try:
                value=conf.get("data",item)
            except:
                try:
                    value=getattr(Env_data,item)
                except AssertionError:
                    continue
            data=data.replace("#{}#".format(item),value)
    return data


#将excel中的被mark的进行替换
def replace_mark_with_data(case,mark,real_data):
    for key,value in case.items():
        if value is not None and isinstance(value,str):
            if value.find(mark)!=-1:#find方法如果找不到指定的字符串会返回-1
                case[key]=value.replace(mark,real_data)
    return case

if __name__ == '__main__':
    case = {
        "method": "POST",
        "url": "http://api.lemonban.com/futureloan/#phone#/member/register",
        "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "美丽可爱的小简"}',
        "msg":"#idid#"
    }
    # if case["request_data"].find("#phone#") != -1:
    #     case = replace_mark_with_data(case, "#phone#", "123456789001")
    # for key, value in case.items():
    #     print(key, value)
    # res=replace_mark_with_data(case,"#phone#","123456789001")
    # for key,value in case.items():
    #     print(key,value)
    res=replace_mark_with_regular(case)
    print(res)
