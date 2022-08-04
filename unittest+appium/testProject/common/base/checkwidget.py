# -*- coding: UTF-8 -*-
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from testProject.common.base.basepage import BasePage
from testProject.common.base.log_output_settings import LogOutputSettings
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class CheckWidget(BasePage):

    @LogOutputSettings.log
    # 检测控件是否存在
    def checkWidget_exist(self, time, expected, element):
        global exist_actual
        try:
            WebDriverWait(driver=self.driver, timeout=time, ignored_exceptions=True).until(
                lambda _: self.locator(AppiumBy.ANDROID_UIAUTOMATOR, element)
            )
            if self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, element).__len__() >= 1:
                exist_actual = True
            else:
                exist_actual = False

        except Exception as e:
            print(e)
            exist_actual = False

        finally:
            if exist_actual == expected:
                print("检查点通过")
                print("实际结果：%s   预期结果：%s" % (exist_actual, expected))
            else:
                print("检查点不通过")
                print("实际结果：%s   预期结果：%s" % (exist_actual, expected))
                raise ValueError("实际结果与预期结果不一致！")

    @LogOutputSettings.log
    # 检查控件属性值
    def checkWidget_property(self, time, expected, attribute, element):
        global property_actual
        try:
            widget = self.locator(AppiumBy.ANDROID_UIAUTOMATOR, element)
            WebDriverWait(driver=self.driver, timeout=time, ignored_exceptions=True).until(
                lambda _: widget
            )
            property_actual = widget.get_attribute(attribute)
            # print(actual)

        except Exception as e:
            print(e)

        finally:
            if property_actual == expected:
                print("检查点通过")
                print("实际结果：%s   预期结果：%s" % (property_actual, expected))
            else:
                print("检查点不通过")
                print("实际结果：%s   预期结果：%s" % (property_actual, expected))
                raise ValueError("实际结果与预期结果不一致！")

    @LogOutputSettings.log
    # 检查toast弹框
    def checkWidget_toast(self, time, expected, element):
        global toast_actual
        try:
            toast = WebDriverWait(driver=self.driver, timeout=time, ignored_exceptions=True).until(
                        EC.presence_of_element_located(('xpath', element))
                    )
            print("toast.text: %s" % toast.text)

            if toast:
                toast_actual = True
            else:
                toast_actual = False

        except NoSuchElementException as e:
            print(e)
            toast_actual = False

        finally:
            if toast_actual == expected:
                print("检查点通过")
                print("实际结果：%s   预期结果：%s" % (toast_actual, expected))
            else:
                print("检查点不通过")
                print("实际结果：%s   预期结果：%s" % (toast_actual, expected))
                raise ValueError("实际结果与预期结果不一致！")
