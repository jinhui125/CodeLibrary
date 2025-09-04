import time
from utils.helpers import load_yaml_file
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from config.settings import BROWSER, HEADLESS, IMPLICIT_WAIT, EXPLICIT_WAIT, chrome_options

test_data = load_yaml_file(file_path='./test_data/test_data.yaml')
options = chrome_options()
driver = webdriver.Chrome(service=ChromeService(executable_path='./chromeDriver_lib/chromedriver.exe'), options=options)

def user_login():
        login_page = LoginPage(driver=driver)
        login_page.scan_code_login() # 等待用户扫码登录
        time.sleep(10)

if __name__ == '__main__':
        user_login()
        