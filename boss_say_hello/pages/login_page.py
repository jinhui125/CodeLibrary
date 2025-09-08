from .base_page import BasePage
from .check_element import CheckElement
from utils import helpers
from setElement_lib.loginPage_elements import LoginPageElements

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.check_element = CheckElement(driver=driver)

    # 打开登录网站
    def open(self, website_url):
        # self.driver.get('https://login.zhipin.com/')
        self.driver.get(website_url)

    # 点击我要招聘按钮
    def click_recruit_btn(self):
        self.click(locator=LoginPageElements.recruit_btn.value)

    # 点击微信扫码登录按钮
    def click_wx_scanCode_btn(self):
        self.click(locator=LoginPageElements.wx_scan_code_btn.value)

    # 输入登录手机号
    def enter_phone_number(self, phone_number):
        self.send_keys(locator=LoginPageElements.phoneNum_inputBox.value, text=phone_number)

    # 点击发送验证码按钮
    def click_send_authCode_btn(self):
        self.click(locator=LoginPageElements.sendAuthCode_btn.value)

    # 输入手机验证码
    def enter_auth_code(self, text_description):
        # self.send_keys(locator=LoginPageElements.authCode_inputBox.value, text=auth_code)
        self.input_keys(locator=LoginPageElements.authCode_inputBox.value, text_description=text_description)

    # 点击用户协议勾选框
    def click_userAgreet_checkBox(self):
        self.click(locator=LoginPageElements.userAgreement_checkBox.value)
    
    # 加载二维码图片
    def qr_code_loading(self):
        self.is_element_existed(locator=LoginPageElements.QR_code.value)

    # 用户登录【验证码方式登录】
    def auth_code_login(self, phone_number):
        self.open()
        self.click_recruit_btn()
        self.enter_phone_number(phone_number=phone_number)
        self.click_send_authCode_btn()
        self.enter_auth_code(text_description='请输入手机接收到的验证码')
        self.click_userAgreet_checkBox()
        self.click(locator=LoginPageElements.login_btn.value)

    # 用户登录【扫码方式登录】
    def scan_code_login(self):
        self.open()
        self.click_recruit_btn()
        self.click_wx_scanCode_btn()
        print('已打开登录页面，请等待二维码加载...')
        self.qr_code_loading()
        self.check_element.check_element_existed(locator=LoginPageElements.QR_code.value, expected_value=True)
        print('二维码已加载，请使用微信扫码登录...')
        self.wait_element_disappear(locator=LoginPageElements.QR_code.value)
        self.check_element.check_element_existed(locator=LoginPageElements.QR_code.value, expected_value=False)



        