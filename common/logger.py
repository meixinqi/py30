import logging
import os.path
import time
from common.handle_ini import conf


BASE_PATTH= os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_path=os.path.join(BASE_PATTH,'log')
if not os.path.exists(LOG_path):
    os.mkdir(LOG_path)
#python 默认打印warning级别以上的日志信息
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='[%Y-%m_%d %H:%M:%S]',
#                     filename='./my.log',
#                     filemode='w')
# logging.critical('this is a critical level')
# logging.error('this is a error level')
# logging.warning('this is a warning level')
# logging.info('this is a info level')
# logging.debug('this is a debug level')
class Logger():
    def __init__(self):
        self.logname=os.path.join(LOG_path,"{}.log".format(time.strftime("%y%m%d")))
        self.logger=logging.getLogger('log')
        self.logger.setLevel(level=logging.DEBUG)
        #self.logger.setLevel(conf.get('log','level'))#从log.ini文件中动态获取
        self.formatter=logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

        #初始化日志文件对象
        handler=logging.FileHandler(self.logname,encoding='utf-8')
        handler.setLevel(level=logging.DEBUG)
        handler.setFormatter(self.formatter)
        #初始化控制台对象
        console=logging.StreamHandler()
        console.setLevel(level=logging.DEBUG)
        console.setFormatter(self.formatter)

        #添加日志文件和控制台对象
        self.logger.addHandler(handler)
        self.logger.addHandler(console)

logger=Logger().logger
if __name__ == '__main__':
    logger.info("---测试开始---")
    logger.debug("---测试结束---")