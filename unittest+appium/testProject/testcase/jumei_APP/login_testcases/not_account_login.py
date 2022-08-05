# -*- coding: UTF-8 -*-
"""
@项目名 ：appium1
@文件名    ：normal_login.py
@开发环境     ：PyCharm
@作者  ：jinHui
@日期    ：2022/7/30 18:17
@测试用例名称：聚美App-不输入账号-登录测试
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
    def test_not_account_login(self):
        # 测试步骤
        login = JuMei(driver=self.driver)
        login.login(page="login_input")

        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Protocol_button.value)
        login.click_enter(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Password_input.value,
                          string=AccountLibrary.JuMei_password.value)

        # 检查点1
        CheckWidget(driver=self.driver).checkWidget_property(element=LoginPageElement.Login_button.value, time=3,
                                                             attribute="enabled", expected="false")

        login.click_enter(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Account_input.value,
                          string=AccountLibrary.JuMei_account.value)

        # 检查点2
        CheckWidget(driver=self.driver).checkWidget_property(element=LoginPageElement.Login_button.value, time=3,
                                                             attribute="enabled", expected="true")

