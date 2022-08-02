# -*- coding: UTF-8 -*-
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from testProject.common.base.basepage import BasePage


class CheckWidget(BasePage):

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

        except Exception:
            exist_actual = False

        finally:
            if exist_actual == expected:
                print("检查点通过")
            else:
                print("检查点不通过")
                raise ValueError("实际结果与预期结果不一致！")

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
            else:
                print("检查点不通过")
                raise ValueError("实际结果与预期结果不一致！")
