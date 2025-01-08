from logging import getLogger, FileHandler, DEBUG
from logging import Formatter
import datetime
import os

# 時刻関係の処理
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

d = now.strftime('%Y_%m%d_%H%M%S_')


class MyLogger():
    def __init__(self, log_file_name="python", output_dir='log'):
        print('create instance MyLogger')
        print(f'log_file_name;{log_file_name} output_dir:{output_dir}')
        self.log_file_name = os.path.join(output_dir, f'{log_file_name}_{d}.log')

        if not (os.path.isdir(output_dir)):
            os.mkdir(output_dir)

        self.logger = getLogger(__name__)  # logging.Loggerのインスタンスを取得
        self.handler = FileHandler(self.log_file_name)
        self.handler.setLevel(DEBUG)
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(self.handler)
        self.formatter = Formatter('[%(levelname)s]%(asctime)s-[(%(filename)s) %(funcName)s(%(lineno)s)]%(message)s')
        self.handler.setFormatter(self.formatter)
        print(f'LogFile : {self.log_file_name}')


if __name__ == '__main__':
    myLogger = MyLogger('MyLogger')
    logger = myLogger.logger
    logger.debug('test')
