# -*- coding: UTF-8 -*-
from enum import Enum


class LoginPageElement(Enum):

    # 手机注册/登录
    Phone_registration_or_login_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/tab_login_phone")'
    # 账号密码登录
    Account_password_login_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/tab_login_account")'
    # 手机号/邮箱/用户名
    Account_input = 'new UiSelector().resourceId("com.jm.android.jumei:id/lg_user_name")'
    # 6-16位密码
    Password_input = 'new UiSelector().resourceId("com.jm.android.jumei:id/lg_password")'
    # 《聚美用户协议》、《聚美隐私权政策》
    Protocol_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/license_select")'
    # 登录
    Login_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/login_account")'
