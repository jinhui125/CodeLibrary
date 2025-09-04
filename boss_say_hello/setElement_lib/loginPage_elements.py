from enum import Enum
from selenium.webdriver.common.by import By

class LoginPageElements(Enum):

    # 微信扫码登录按钮
    wx_scan_code_btn = (By.CSS_SELECTOR, '.wx-login-btn')
    # 我要招聘按钮li[ka="signup_boss_tab_click"]
    recruit_btn = (By.CSS_SELECTOR, '.identity-tab li:last-child')
    # 手机号输入框
    phoneNum_inputBox = (By.CSS_SELECTOR, 'input[placeholder="手机号"]')
    # 发送验证码按钮
    sendAuthCode_btn = (By.CSS_SELECTOR, '.btn-sms')
    # 短信验证码输入框
    authCode_inputBox = (By.CSS_SELECTOR, 'input[placeholder="短信验证码"]')
    # 登录按钮
    login_btn = (By.CSS_SELECTOR, '.sure-btn')
    # 用户协议勾选按钮
    userAgreement_checkBox = (By.CSS_SELECTOR, '.agree-policy')
    # 登录二维码
    QR_code = (By.CSS_SELECTOR, '.mini-qrcode')