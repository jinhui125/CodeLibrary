# -*- coding: UTF-8 -*-

from testProject.common.base.deviceconfig import deviceConnect
from appium.webdriver.common.appiumby import AppiumBy
from testProject.common.module.jumei_element.main_page import MainPageElement
from selenium.webdriver.support.ui import WebDriverWait

driver = deviceConnect(deviceName='127.0.0.1:62001', appPackage="", appActivity="")


# element_list = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, MainPageElement.Commodity_type_selection_button.value)


def swipe_find_element(dr, string, elements_value, start_x, start_y, end_x, end_y):
    element_ls = dr.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, elements_value)
    ls = list(map(lambda x: x.text, element_ls))
    if string in ls:
        return element_ls[ls.index(string)]
    else:
        dr.swipe(start_x, start_y, end_x, end_y)


if __name__ == '__main__':
    element = WebDriverWait(driver, 10, 2).\
        until(lambda x: swipe_find_element(dr=x, string="蜂蜜面膜10片",
                                           elements_value=MainPageElement.Commodity_type_selection_button.value,
                                           start_x=860, start_y=1500, end_x=860, end_y=1250))
    element.click()
