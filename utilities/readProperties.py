# we use this python file to read ini files from config.ini-> Configuration folder

import configparser
import iniconfig

config = configparser.RawConfigParser()
config.read("D:\\pycharm-new projects\\pythonProject1\\pytest-automation\\Configurations\\config.ini")    # -> this is method to read config.ini files

#to access data inside ini file
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        URL = config.get('common info','baseURL')
        return URL

    @staticmethod
    def getUserName():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password

    @staticmethod
    def getWrongPassword():
        Wrong_password = config.get('common info','password1')
        return Wrong_password



