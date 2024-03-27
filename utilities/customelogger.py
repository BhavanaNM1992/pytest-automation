import logging
import Logs

class LogGen:
    @staticmethod
    def logging():
        logging.basicConfig(filename="D:\\pycharm-new projects\\pythonProject1\\pytest-automation\\Logs\\automation.log",
                            format='%(asctime)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger



