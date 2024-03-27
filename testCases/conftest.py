from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import iniconfig
import pytest

@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


##################  to generate pytest HTML reports   #############
# def pytest_configure(config):
#     config._metadata['Project Name']='nop Commerce'
#     config._metadata['Module Name']='Customers'
#     config._metadata['Tester']='Bhavana'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("hey",None)
#     metadata.pop("hello",None)