# -*- coding: UTF-8 -*-
"""
@项目名 ：unittest+appium 
@文件名    ：home_interface_inspect_main.py
@开发环境     ：PyCharm 
@作者  ：jinHui
@日期    ：2022/8/6 14:47 
@测试用例名称：聚美App-首页界面检查-测试
"""

import unittest
from testProject.pageObject.jumei import JuMei
from testProject.common.module.jumei_element.main_page import MainPageElement
from testProject.common.base.command import Command
from testProject.common.base.checkwidget import CheckWidget
from testProject.common.base.deviceconfig import deviceConnect
from testProject.common.module.package import PackageInfo


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
    def test_normal_login(self):

        # 测试步骤
        frontPage = JuMei(driver=self.driver)
        frontPage.login(page='not_login_main')

        # 检查点1
        CheckWidget(driver=self.driver).checkWidget_property(element=MainPageElement.Front_page_button.value, time=3,
                                                             attribute="selected", expected="true")
        CheckWidget(driver=self.driver).checkWidget_property(element=MainPageElement.Front_title_button.value, time=3,
                                                             attribute="selected", expected="true")
        CheckWidget(driver=self.driver).checkWidget_property(element=MainPageElement.Classification_button.value, time=3,
                                                             attribute="selected", expected="false")
        CheckWidget(driver=self.driver).checkWidget_property(element=MainPageElement.Duty_free_shop_button.value, time=3,
                                                             attribute="selected", expected="false")
