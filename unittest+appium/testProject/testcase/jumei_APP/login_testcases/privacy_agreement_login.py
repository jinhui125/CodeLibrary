# -*- coding: UTF-8 -*-
"""
@项目名 ：unittest+appium 
@文件名    ：privacy_agreement_login.py
@开发环境     ：PyCharm 
@作者  ：jinHui
@日期    ：2022/8/5 11:36 
@测试用例名称：聚美App-账号登录界面-隐私协议界面跳转测试
"""

import unittest
from appium.webdriver.common.appiumby import AppiumBy
from testProject.common.base.command import Command
from testProject.common.base.deviceconfig import deviceConnect
from testProject.common.module.package import PackageInfo
from testProject.pageObject.jumei import JuMei
from testProject.common.module.jumei_element.login_page import LoginPageElement
from testProject.common.base.checkwidget import CheckWidget


class TestLogin(unittest.TestCase):

    def setUp(self):
        Command.clear_user_data(package=PackageInfo.JuMei_package.value)
        self.driver = deviceConnect(deviceName='127.0.0.1:62001', appPackage=PackageInfo.JuMei_package.value,
                                    appActivity=PackageInfo.JuMei_activity.value)

    def tearDown(self):
        self.driver.quit()
        Command.clear_user_data(package=PackageInfo.JuMei_package.value)

    def test_privacy_agreement_login(self):
        login = JuMei(self.driver)
        login.login(page="login_input")

        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.User_agreement_textLink.value)

        # 检查点1
        CheckWidget(driver=self.driver).checkWidget_exist(element=LoginPageElement.User_agreement_title.value, time=3,
                                                          expected=True)
        CheckWidget(driver=self.driver).checkWidget_exist(element=LoginPageElement.Account_input.value, time=3,
                                                          expected=False)

        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Privacy_agreement_close_button.value)

        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Privacy_textLink.value)

        # 检查点2
        CheckWidget(driver=self.driver).checkWidget_exist(element=LoginPageElement.Privacy_title.value, time=3,
                                                          expected=True)
        CheckWidget(driver=self.driver).checkWidget_exist(element=LoginPageElement.Account_input.value, time=3,
                                                          expected=False)
