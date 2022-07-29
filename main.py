import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

import unittest

from BeautifulReport import BeautifulReport
from common.handle_path import cases_dir,report_dir,case_dir
from common.handle_ini import conf
print(conf.get("serve","base_url"))
# 收集用例

#unittest.TestLoader()用例加载对象，默认执行路径下格式为test_*.py的模块，也可指定特定的模块
s = unittest.TestLoader().discover(cases_dir,pattern="test_login.py")

#生成报告
br = BeautifulReport(s)
br.report("py30-注册用例自动化", "report_.html",report_dir)
   # 一个入口，全部执行
# if __name__ == '__main__':
#     unittest.main