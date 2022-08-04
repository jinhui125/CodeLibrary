# -*- coding: UTF-8 -*-
"""
@项目名 ：appium+unittest
@文件名    ：wrong_account_login.py
@开发环境     ：PyCharm
@作者  ：jinHui
@日期    ：2022/7/30 18:17
@测试用例名称：聚美App-错误账号登录-登录测试
"""
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from testProject.pageObject.jumei import JuMei
from testProject.common.base.command import Command
from testProject.common.base.checkwidget import CheckWidget
from testProject.common.module.jumei_element.login_page import LoginPageElement
from testProject.common.base.deviceconfig import deviceConnect
from testProject.common.module.package import PackageInfo


class TestLogin(unittest.TestCase):

    # 预置条件
    def setUp(self):
        Command.adb_command(command="adb shell pm clear com.jm.android.jumei")
        Command.adb_command(command="adb shell pm clear com.jm.android.jumei")
        self.driver = deviceConnect(deviceName='127.0.0.1:62001', appPackage=PackageInfo.JuMei_package.value,
                                    appActivity=PackageInfo.JuMei_activity.value)

    # 收尾条件
    def tearDown(self):
        self.driver.quit()
        Command.adb_command(command="adb shell pm clear com.jm.android.jumei")

    # 测试用例
    def test_not_password_login(self):
        # 测试步骤
        login = JuMei(driver=self.driver)
        login.login(page="login_input")

        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Protocol_button.value)
        login.click_enter(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Account_input.value, string="1111111")

        login.click_enter(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Password_input.value, string="jh739140236")
        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Login_button.value)

        # 检查点1
        CheckWidget(driver=self.driver).checkWidget_toast(element=LoginPageElement.toast.value, time=5,
                                                          expected=True)
