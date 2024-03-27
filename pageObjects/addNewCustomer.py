import random
import string
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class addNewCustomer:
    hrefCustomer_menu_xpath ="//a[@href='#']//p[contains(text(),'Customers')]"
    customerItem_xpath ="//a[@href='/Admin/Customer/List']//p"
    btn_addnewCustomer_xpath ="//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtpassword_id = "Password"
    txtFirstName_id = "FirstName"
    txtLastName_id ="LastName"
    rdMalebutton_id = "Gender_Male"
    rdfemalebutton_id= "Gender_Female"
    textDOB_id="DateOfBirth"
    btn_calender_xpath ="//span[@class='k-icon k-i-calendar']"
    txtcompany_name_id = "Company"
    clickbox_is_tax_exempt_id = "IsTaxExempt"
    txt_admin_comment_id ="AdminComment"
    clickbox_active_id = "Active"
    lstCustomer_role_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstAdministrator_xpath = "//li[contains(text(),'Administrators')]"
    lstForum_Moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstGuests_xpath="//span[contains(text(),'Guests')]"
    selet_Vendor_id = "VendorId"
    txt_Newletter_xpath ="//input[@class='k-input k-readonly']"
    btn_save_name_xpath = "//button[@name='save']"
    successfull_message_xpath1 = "//div[@class='alert alert-success alert-dismissable']"
    successfull_message_xpath = "body"


    def __init__(self,driver):
        self.driver =driver

    def clickCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.hrefCustomer_menu_xpath).click()

    def clickCustomerItem(self):
        self.driver.find_element(By.XPATH, self.customerItem_xpath).click()

    def ClickAddNewCustomer(self):
        self.driver.find_element(By.XPATH,self.btn_addnewCustomer_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.txtpassword_id).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lastname)

    def setCustomerrole(self,role):
        #self.driver.find_element(By.XPATH,self.lstCustomer_role_xpath).clear()
        self.driver.find_element(By.XPATH, self.lstCustomer_role_xpath).click()
        if role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH,self.lstAdministrator_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstForum_Moderators_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click()",self.listitem)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.rdMalebutton_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,self.rdfemalebutton_id).click()
        else:
            self.driver.find_element(By.ID, self.rdfemalebutton_id).click()

    def setDate(self,date):
        self.driver.find_element(By.ID,self.textDOB_id).click()
        self.driver.find_element(By.ID, self.textDOB_id).send_keys(date)

    def setCompanyName(self,companyname):
        self.driver.find_element(By.ID,self.txtcompany_name_id).send_keys(companyname)

    def setSaveButton(self):
        self.driver.find_element(By.XPATH,self.btn_save_name_xpath).click()

    # def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    #     return ''.join(random.choice(chars) for x in range(size))










