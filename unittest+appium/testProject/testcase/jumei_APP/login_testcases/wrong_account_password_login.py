# -*- coding: UTF-8 -*-
"""
@项目名 ：appium+unittest
@文件名    ：wrong_account_password_login.py
@开发环境     ：PyCharm
@作者  ：jinHui
@日期    ：2022/7/30 18:17
@测试用例名称：聚美App-错误账号或者密码登录-登录测试
"""
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from testProject.pageObject.jumei import JuMei
from testProject.common.base.command import Command
from testProject.common.base.checkwidget import CheckWidget
from testProject.common.module.jumei_element.login_page import LoginPageElement
from testProject.common.base.deviceconfig import deviceConnect
from testProject.common.module.package import PackageInfo
from testProject.testdata.accountLibrary import AccountLibrary


class TestLogin(unittest.TestCase):

    # 预置条件
    def setUp(self):
        Command.clear_user_data(package=PackageInfo.JuMei_package.value)
        self.driver = deviceConnect(deviceName='127.0.0.1:62001', appPackage=PackageInfo.JuMei_package.value,
                                    appActivity=PackageInfo.JuMei_activity.value)

    # 收尾条件
    def tearDown(self):
        self.driver.quit()
        Command.clear_user_data(package=PackageInfo.JuMei_package.value)

    # 测试用例
    def test_wrong_account_password_login(self):
        # 测试步骤
        login = JuMei(driver=self.driver)
        login.login(page="login_input")

        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Protocol_button.value)
        login.click_enter(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Account_input.value, string="1111111")

        login.click_enter(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Password_input.value,
                          string=AccountLibrary.JuMei_password.value)
        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Login_button.value)

        # 检查点1
        CheckWidget(driver=self.driver).checkWidget_toast(element=LoginPageElement.toast.value, time=5,
                                                          expected=True)

        login.clear(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Account_input.value,
                    sort="clear_enter", string=AccountLibrary.JuMei_account.value)
        login.clear(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Password_input.value,
                    sort="clear_enter", string="1111111")
        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Login_button.value)

        # 检查点2
        CheckWidget(driver=self.driver).checkWidget_toast(element=LoginPageElement.toast.value, time=5,
                                                          expected=True)

