# -*- coding: UTF-8 -*-
"""
@项目名 ：appium+unittest
@文件名    ：normal_login.py
@开发环境     ：PyCharm
@作者  ：jinHui
@日期    ：2022/7/30 18:17
@测试用例名称：聚美App-正常-登录测试
"""
import unittest
from testProject.pageObject.jumei import JuMei
from testProject.common.module.jumei_element.my_page import MyPageElement
from testProject.common.base.command import Command
from testProject.common.base.checkwidget import CheckWidget
from testProject.common.base.deviceconfig import deviceConnect
from testProject.common.module.package import PackageInfo


class TestLogin(unittest.TestCase):

    # 预置条件
    def setUp(self):
        Command.adb_command(command="adb shell pm clear com.jm.android.jumei")
        self.driver = deviceConnect(deviceName='127.0.0.1:62001', appPackage=PackageInfo.JuMei_package.value,
                                    appActivity=PackageInfo.JuMei_activity.value)

    # 收尾条件
    def tearDown(self):
        self.driver.quit()
        Command.adb_command(command="adb shell pm clear com.jm.android.jumei")

    # 测试用例
    def test_normal_login(self):

        # 测试步骤
        login = JuMei(driver=self.driver)
        login.login_account(account="15623271191", password="jh739140236", page="login")

        # 检查点
        CheckWidget(driver=self.driver).checkWidget_exist(element=MyPageElement.Member_entry_button.value, time=3,
                                                          expected=True)
        CheckWidget(driver=self.driver).checkWidget_exist(element=MyPageElement.Registration_or_login_button.value,
                                                          time=3, expected=False)
