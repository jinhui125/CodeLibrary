from .base_page import BasePage, BaseAssert

class CheckElement(BasePage, BaseAssert):
    
    def __init__(self, driver):
        super().__init__(driver)

    # 判断单个元素的存在是否符合预期值
    def check_element_existed(self, locator, expected_value):
        try:
            __exist_flag = True
            if self.is_element_existed(locator=locator):
                __exist_flag = True
            else:
                __exist_flag  = False
        
        except Exception as error:
            __exist_flag = False

        finally:
            self.define_assert(real_result=__exist_flag, expected_result=expected_value)

    # 判断多个元素的存在是否符合预期值
    def check_elements_existed(self, locator, expected_value):
        try:
            __exist_flag = True
            if self.is_elements_existed(locator=locator):
                __exist_flag = True
            else:
                __exist_flag  = False
        
        except Exception as error:
            __exist_flag = False

        finally:
            self.define_assert(real_result=__exist_flag, expected_result=expected_value)

    # 判断元素的属性值是否符合预期值
    def check_element_attribute(self, locator, attribute_name, expected_value):
        try:
            __attribute_flag = True
            if self.is_element_existed(locator=locator):
                __attribute_flag = self.find_element(locator=locator).get_attribute(name=attribute_name)
                self.define_assert(real_result=__attribute_flag, expected_result=expected_value)

        except Exception as error:
            raise error
    
    # 判断是否有气泡弹框出现
    def check_element_toast(self, locator, expected_value):
        try:
            __toast_flag = True
            if self.is_element_present(locator=locator):
                __toast_flag = True

        except Exception as error:
            __toast_flag = False
            raise error
        
        finally:
            self.define_assert(real_result=__toast_flag, expected_result=expected_value)
