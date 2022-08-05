# -*- coding: UTF-8 -*-
"""
@项目名 ：unittest+appium 
@文件名    ：third_party_account_login.py
@开发环境     ：PyCharm 
@作者  ：jinHui
@日期    ：2022/8/5 20:18 
@测试用例名称：聚美App-第三方账号跳转-登录测试
"""

import unittest
from appium.webdriver.common.appiumby import AppiumBy
from testProject.common.module.jumei_element.login_page import LoginPageElement
from testProject.common.base.checkwidget import CheckWidget
from testProject.common.base.command import Command
from testProject.common.module.package import PackageInfo
from testProject.common.base.deviceconfig import deviceConnect
from testProject.pageObject.jumei import JuMei


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        Command.clear_user_data(package=PackageInfo.JuMei_package.value)
        self.driver = deviceConnect(deviceName='127.0.0.1:62001', appPackage=PackageInfo.JuMei_package.value,
                                    appActivity=PackageInfo.JuMei_activity.value)

    def tearDown(self) -> None:
        self.driver.quit()
        Command.clear_user_data(package=PackageInfo.JuMei_package.value)

    def test_third_party_account_login(self):
        login = JuMei(driver=self.driver)
        login.login(page='login_input')

        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.Weibo_imageLink.value)

        # 检查点1
        CheckWidget(driver=self.driver).checkWidget_exist(element=LoginPageElement.Weibo_title.value, time=6,
                                                          expected=True)
        CheckWidget(driver=self.driver).checkWidget_exist(element=LoginPageElement.Third_party_account_title.value,
                                                          time=6, expected=False)

        login.back()

        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.QQ_imageLink.value)

        # 检查点2
        CheckWidget(driver=self.driver).checkWidget_exist(element=LoginPageElement.QQ_downLoad_button.value, time=6,
                                                          expected=True)
        CheckWidget(driver=self.driver).checkWidget_exist(element=LoginPageElement.Third_party_account_title.value,
                                                          time=6, expected=False)
        login.back()

        login.click(AppiumBy.ANDROID_UIAUTOMATOR, LoginPageElement.ZhiFuBao_imageLink.value)

        # 检查点3
        CheckWidget(driver=self.driver).checkWidget_exist(element=LoginPageElement.ZhiFuBao_title.value, time=6,
                                                          expected=True)
        CheckWidget(driver=self.driver).checkWidget_exist(element=LoginPageElement.Third_party_account_title.value,
                                                          time=6, expected=False)
        login.back()



