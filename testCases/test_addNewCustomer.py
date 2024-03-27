import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from pageObjects.addNewCustomer import addNewCustomer
from utilities.readProperties import ReadConfig
from utilities.customelogger import LogGen
import random
import string

import time

class Test_003_addcustomer:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(8))

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_addNewCustomer(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #adding new customer

        self.addcust = addNewCustomer(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerItem()
        self.addcust.ClickAddNewCustomer()



        #### adding new customer details

        self.email = self.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        # self.addcust.setEmail("bhavanavalahatti@gmailnm.com")
        self.addcust.setPassword("Frontech@12")
        self.addcust.setFirstName("Bhavana")
        self.addcust.setLastName("Valahatti")
        self.addcust.setGender("Female")
        self.addcust.setDate("3/28/2024")
        self.addcust.setCompanyName("Accenture")
        self.addcust.setCustomerrole("Forum Moderators")
        self.addcust.setSaveButton()


        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True==True
        else:
            assert True==False






