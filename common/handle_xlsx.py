#加载工作簿，读取sheet，获取单元格信息
import json
import os.path

from openpyxl  import load_workbook
from common.handle_path import case_dir
class Handle_xlsx:
    def __init__(self,file_path,sheet_name):
        self.wb=load_workbook(file_path)
        self.ws=self.wb[sheet_name]
    def read_xlsx(self):
        #第一步，读取title
        titles=[]
        #print(list(self.ws.rows)[0])
        for cel in list(self.ws.rows)[0]:
            titles.append(cel.value)
        #第二步，读取数据行
        all_datas=[]
        for row in list(self.ws.rows)[1:]:#获取每一行，每一行都是个元组
            #print(row)
            row_datas=[]
            for index in range(len(row)):#遍历每个元组成员
                row_datas.append(row[index].value)  # 获取成员的值
            # for cel in row:
            #     row_datas.append(cel.value)
            res=dict(zip(titles,row_datas))#每行数据组合成字典
            #res['request']=json.loads(res['request'])##将请求数据从json字符串转换成字典对象。
            all_datas.append(res)
        return all_datas
    def close_file(self):
        self.wb.close()


if __name__ == '__main__':
    file_path=os.path.join(case_dir,'api_cases.xlsx')
    a=Handle_xlsx(file_path,'注册')
    print(a.read_xlsx())

