from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:
    inputbox_email_id= "Email"
    inputbox_password_id="Password"
    login_button_xpath= "//button[@class='button-1 login-button']"
    logout_link_text = "Logout"


    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.inputbox_email_id).clear()
        self.driver.find_element(By.ID,self.inputbox_email_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.inputbox_password_id).clear()
        self.driver.find_element(By.ID,self.inputbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_link_text).click()





