import os.path
import yaml

class Handle_yml:
    def read_yml(self,file_path):
        with open(file_path,encoding='utf-8')as fs:
            data=yaml.load(fs,yaml.FullLoader)
            return data
yml_data=Handle_yml()

if __name__ == '__main__':

    file_path=os.path.join(os.path.abspath('..'),'data','login.yml')
    yml_data = Handle_yml()
    data=yml_data.read_yml(file_path)
    print(data)