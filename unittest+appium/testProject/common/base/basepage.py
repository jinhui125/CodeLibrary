# -*- coding: UTF-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from testProject.common.base.log_output_settings import LogOutputSettings


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @LogOutputSettings.log
    def locator(self, *element):
        """locator()方法
            定义：定位元素
            使用方法：BasePage().locator(*element)
            参数含义：element：需要操作的元素
        """
        return self.driver.find_element(element[0], element[1])

    @LogOutputSettings.log
    def locators(self, *element):
        """locators()方法
            定义：定位同类型的多个元素
            使用方法：BasePage().locator(*element)
            参数含义：element：需要操作的元素
        """
        return self.driver.find_elements(element[0], element[1])

    @LogOutputSettings.log
    def wait_element(self, *element, time):
        """wait_element()方法
            定义：显示等待元素出现
            使用方法：BasePage.wait_element(element, time)
            参数含义：element：需要操作的元素；time：等待时间
        """
        WebDriverWait(driver=self.driver, timeout=time).until(
            lambda _: self.driver.find_element(element[0], element[1])
        )

    @LogOutputSettings.log
    def click(self, *element):
        """click()方法
            定义：元素点击操作
            使用方法：BasePage().click(*element)
            参数含义：element：需要操作的元素
        """
        self.wait_element(*element, time=1)
        self.locator(*element).click()

    @LogOutputSettings.log
    def input(self, string, *element):
        """input()方法
            定义：元素输入操作
            使用方法：BasePage().input(element, string)
            参数含义：element：需要操作的元素；string：需要输入的字符串
        """
        self.wait_element(*element, time=1)
        self.locator(*element).send_keys(string)

    @LogOutputSettings.log
    def click_enter(self, *element, string):
        """click_enter()方法
            定义：点击元素并输入
            使用方法：BasePage().click_enter(element, string)
            参数含义：element：需要操作的元素；string：需要输入的字符串
        """
        self.click(*element)
        self.input(string, *element)

    @LogOutputSettings.log
    def clear(self, *element, **kwargs):
        """clear()方法
            定义：清除文本框内容并输入或者清除文本框内容
            使用方法：BasePage().clear(sort, string, element)
            参数含义：element：需要操作的元素；sort：行为种类；string：需要输入的字符串
        """
        if kwargs["sort"] == "clear_enter":   # 清除文本框的内容并输入新的字符串
            self.locator(*element).clear()
            self.click_enter(string=kwargs["string"], *element)
        elif kwargs["sort"] == "edit_clear":  # 清除文本框的内容
            self.locator(*element).clear()
        else:
            raise ValueError("clear_enter方法中的参数sort值错误")

    @LogOutputSettings.log
    def back(self):
        """back()方法
            定义：返回上一级页面
            使用方法：BasePage().back()
        """
        self.driver.back()

    # @LogOutputSettings.log
    # def byText_swipe_find_sameElement(self, string, *element, start_x, start_y, end_x, end_y):
    #     """byText_swipe_find_sameElement()方法
    #         定义：通过文本滑动查找同种类型元素中指定元素
    #         使用方法：BasePage().byText_swipe_find_sameElement(string, *element, start_x, start_y, end_x, end_y)
    #         参数含义：element：需要查找的元素；string：指定元素的文本；start_x：滑动的起始x轴坐标, start_y：滑动的起始y轴坐标,
    #                 end_x：滑动的结束x轴坐标, end_y：滑动的结束y轴坐标
    #     """
    #     element_ls = self.locators(*element)
    #     ls = list(map(lambda x: x.text, element_ls))
    #     if string in ls:
    #         return element_ls[ls.index(string)]
    #     else:
    #         self.driver.swipe(start_x, start_y, end_x, end_y)


