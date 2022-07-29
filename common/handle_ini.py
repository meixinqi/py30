import os.path
from configparser import ConfigParser
#file_path=os.path.join(os.path.abspath('..'),'config','log.ini')
file_path="D:\DD\python3\pythonProject\learn_unit\config\log.ini"
class Handle_logconfig(ConfigParser):
    def __init__(self,filepath):
        super().__init__()
        self.read(file_path,encoding='utf-8')

conf=Handle_logconfig(file_path)

if __name__ == '__main__':
    print(conf.get("mysql","host"))