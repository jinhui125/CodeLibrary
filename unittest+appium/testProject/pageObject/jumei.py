# -*- coding: UTF-8 -*-
from appium.webdriver.common.appiumby import AppiumBy
from testProject.common.base.basepage import BasePage
from testProject.common.module.jumei_element.start_page import StartPageElement
from testProject.common.module.jumei_element.login_page import LoginPageElement
from testProject.common.module.jumei_element.main_page import MainPageElement
from testProject.common.module.jumei_element.my_page import MyPageElement


class JuMei(BasePage):

    # 登录账号
    def login_account(self, account="", password="", page=""):
        """
        login_account()方法
            定义：登录操作
            使用方法：JuMei().login_account(account, password, page)
            参数含义：account：账号字符串
                    password：密码字符串
                    page：停留的界面
                        page-value：login：完成登录；login_main：登录成功并停留在首页界面；login_classification：登录成功并停留在分类界面
                                  login_shoppingCart：登录成功并停留在购物车界面；not_login_main：未完成登录并停留在首页界面；
                                  not_login_classification：未完成登录并停留在分类界面；not_login_shoppingCart：未完成登录并停留在购物车界面

        """
        try:
            if page == "login":  # 完成登录
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, StartPageElement.Agree_continue_button.value)
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, StartPageElement.Allow_permission_button.value)
                self.wait_element(AppiumBy.ANDROID_UIAUTOMATOR, MainPageElement.My_button.value, time=8)
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, MainPageElement.My_button.value)
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, MyPageElement.Registration_or_login_button.value)
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Account_password_login_button.value)
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Protocol_button.value)
                self.click_enter(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Account_input.value, string=account)
                self.click_enter(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Password_input.value, string=password)
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Login_button.value)
            elif page == "login_main":  # 登录状态-首页界面
                self.login_account(account, password, page="login")
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, MainPageElement.Front_page_button.value)
            elif page == "login_classification":  # 登录状态-分类界面
                self.login_account(account, password, page="login")
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, MainPageElement.Classification_button.value)
            elif page == "login_shoppingCart":  # 登录状态-购物车界面
                self.login_account(account, password, page="login")
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, MainPageElement.Shopping_cart_button.value)

            elif page == "not_login_main":  # 未登录状态-首页界面
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, StartPageElement.Agree_continue_button.value)
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, StartPageElement.Allow_permission_button.value)
                self.wait_element(AppiumBy.ANDROID_UIAUTOMATOR, MainPageElement.My_button.value, time=8)
            elif page == "not_login_classification":  # 未登录状态-分类界面
                self.login_account(account, password, page="not_login_main")
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, MainPageElement.Classification_button.value)
            elif page == "not_login_shoppingCart":  # 未登录状态-购物车界面
                self.login_account(account, password, page="not_login_main")
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, MainPageElement.Shopping_cart_button.value)
            elif page == "not_login_my":  # 未登录状态-我的界面
                self.login_account(account, password, page="not_login_main")
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, MainPageElement.My_button.value)

            elif page == "login_input":  # 登录输入账号密码界面
                self.login_account(account, password, page="not_login_my")
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, MyPageElement.Registration_or_login_button.value)
                self.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Account_password_login_button.value)

        except Exception as e:
            print(e)
