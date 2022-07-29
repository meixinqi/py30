# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# import unittest
# import time
from common.handle_ini import conf
# from HTMLTestRunner import HTMLTestRunner
# from common.handle_path import case_url,report_url
# discover=unittest.TestLoader().discover(case_url,pattern='test*.py')
#
# if __name__ == '__main__':
#     #执行测试用例
#     # runner=unittest.TextTestRunner()
#     # runner.run(discover)
#     #执行测试用例并生成测试报告
#     # with open("report3.html",'wb')as fs:
#     #     runner=HTMLTestRunner(fs,title='第一个htmlrunner')
#     #     runner.run(discover)
#     #执行测试用例并生成测试报告
#     from BeautifulReport import BeautifulReport
#     br=BeautifulReport(discover)
#     br.report('单元测试框架unittest的报告',"{}.html".format(time.strftime("%y%m%d")),report_url)


import unittest
import os
from BeautifulReport import BeautifulReport
from common.handle_path import cases_dir,report_dir
from common.handle_ini import conf

# 收集用例

s = unittest.TestLoader().discover(cases_dir)

# 生成报告
br = BeautifulReport(s)
br.report("py30-注册用例自动化", "report_.html",report_dir)
