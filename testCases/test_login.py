import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customelogger import LogGen

import time

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    password1 = ReadConfig.getWrongPassword()

    # log = LogGen.logging()
    @pytest.mark.sanity
    @pytest.mark.regression

    def test_login(self,setup):
        # self.log.info("***************** verifing login**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # self.log.info("*************8succesfully login****************")
        self.lp.clickLogout()
        self.driver.close()

    def test_wrongcreds(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.lp1 = LoginPage(self.driver)
        self.lp1.setUserName(self.username)
        self.lp1.setPassword(self.password1)
        self.lp1.clickLogin()
        # self.log.info("********** gor wrong creds****************")
        self.driver.save_screenshot("D:\\pycharm-new projects\\pythonProject1\\pytest-automation\\Screenshots\\test_wrongcreds1.png")
        # self.lp.clickLogout()





