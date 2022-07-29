#存在一个名称为data.log的文件，data.log中的内容是以逗号作为分隔符的，依次存储了一次测试的TestID,TestTime,Success(0成功；1失败)。文件 中数据均为非负整数。
# 请写一段程序(不限语言)，对所有成功（Success=0）的测试，输出：
# 1）打印最大、最小TestTime;
# 2）打印平均TestTime，保留小数点2位数。
# data.log的内容格式如下：
# TestID,TestTime,Success
# 0,149,0
# 1,69,0
# 2,45,0
# 3,18,1
# 4,18,1
# test_time=[]
# with open('data.log',mode='r',encoding='utf-8') as fs:
#     for line in fs.readlines()[1:]:
#         line=list(map(int,line.strip().split(',')))
#         if line[2]==0:
#             test_time.append(line[1])
# if len(test_time)>0:
#     avg_testtime=sum(test_time)/len(test_time)
#     max_testtime=max(test_time)
#     min_testtime=min(test_time)
#
# print('最大Testtime是{}，最小Tesrtime是{}，平均Testtime是{}'.format(max_testtime,min_testtime,avg_testtime))
#
# #将列表a = ["h","e","l","l","o"]拼接成字符串，请用多种方法实现
# a=["h","e","l","l","o"]
# # print(''.join(a))
# p=''
# for i in a:
#     p+=i
# print(p)
import hashlib
import random
# aa='A'
# d={'1':'A','2':'B','3':'C','4':'D','5':'E'}

# def md5encode(strs):
#     m=hashlib.md5()
#     m.update(strs)
#     return m.hexdigest()
# for key in d.keys():
#     print(md5encode(aa.encode('utf-8')))

def  max_num(lst):
    p=''
    a=[]
    m=''
    for i in lst:
        p+=str(i)
    for k in p:
       a.append(k)
    m=sorted(a,reverse=True)
    return ''.join(m)

a=filter(lambda x:x%21==0,range(1,201))
print(list(a))