import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#base_url2=os.path.abspath('..')
#测试用例的路径
case_dir=os.path.join(base_dir,'data')
#测试数据的路径
cases_dir=os.path.join(base_dir,'test_cases')
#配置文件路径
conf_dir=os.path.join(base_dir,'config')
#日志输出文件路径
log_dir=os.path.join(base_dir,'log')
#报告输出路径
report_dir=os.path.join(base_dir,'report')