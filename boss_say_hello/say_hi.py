import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.check_element import CheckElement
from setElement_lib.mainPage_elements import MainPageElements
from utils.helpers import *
from selenium.webdriver.chrome.service import Service as ChromeService
from config.settings import BROWSER, HEADLESS, IMPLICIT_WAIT, EXPLICIT_WAIT, chrome_options

test_data = load_yaml_file(file_path='./test_data/condition_data.yaml')
options = chrome_options()
driver = webdriver.Chrome(service=ChromeService(executable_path='./chromeDriver_lib/chromedriver.exe'), options=options)
check_element = CheckElement(driver=driver)
login_page = LoginPage(driver=driver)
main_page = MainPage(driver=driver)
position_name = test_data['FED_engineer'][0]    # 要查找的职位名
condition_ls = test_data['conditionData']   # 简历需要有哪些要求
position_dict = {
                    'FED_engineer': MainPageElements.FED_engineer_btn.value,    # 职位：前端开发工程师
                    'ED_engineer': MainPageElements.ED_engineer_btn.value,      # 职位：电气设计工程师
                    'HN_engineer': MainPageElements.HN_engineer_btn.value,      # 职位：硬件网络工程师
                    'CS_engineer': MainPageElements.CS_engineer_btn.value,      # 职位：悬架工程师
                    'IAED_engineer': MainPageElements.IAED_engineer_btn.value,  # 职位：内外饰设计工程师
                    'VA_engineer': MainPageElements.VA_engineer_btn.value       # 职位：视频标注
                 }

def user_login():
   
    login_page = LoginPage(driver=driver)
    login_page.scan_code_login() # 等待用户扫码登录
    time.sleep(10)  # 等待用户手机验证
    check_element.check_element_existed(locator=MainPageElements.referral_NB_btn.value, expected_value=True)

def handle_filter_condition():
   
    main_page.click_referral_NB_btn()
    main_page.click_job_switch_btn()
    main_page.click_job_selection_list_btn(select_position_name=position_dict[f'{position_name}'])

def handle_candidate_number():

    main_page.filter_candidate_number(candidate_number=60)

def handle_say_hi():
    
    main_page.handle_candidate_resume_info(condition_ls=condition_ls)

if __name__ == '__main__':

    user_login()
    handle_filter_condition()
    handle_candidate_number()
    handle_say_hi()
        