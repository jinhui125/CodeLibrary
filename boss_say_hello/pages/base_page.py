from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.settings import EXPLICIT_WAIT

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=EXPLICIT_WAIT)

    # 查找单个元素
    def find_element(self, locator):
        
        try:
            # 返回匹配到的单个元素信息
            return self.wait.until(EC.visibility_of_element_located(locator=locator))
        except (TimeoutException, NoSuchElementException) as e:
            raise Exception(f'元素{locator}未找到：{str(e)}')

    # 查找多个元素 
    def find_elements(self, locator):

        try:
            # 返回匹配到的所有元素信息
            return self.wait.until(EC.visibility_of_any_elements_located(locator=locator))
        except (TimeoutException, NoSuchElementException) as e:
            raise Exception(f'元素{locator}未找到：{str(e)}')

    # 对元素执行点击操作 
    def click(self, locator):

        element = self.find_element(locator=locator)
        element.click()

    # 对元素执行输入操作
    def send_keys(self, locator, text):

        element = self.find_element(locator=locator)
        element.clear()
        element.send_keys(text)
    
    # 等待用户输入，并将用户输入的东西输出到输入框中
    def input_keys(self, locator, text_description):
        input_text = input(f'{text_description}: ')
        self.send_keys(locator=locator, text=input_text)

    # 获取元素文本内容
    def get_text(self, locator):
        
        element = self.find_element(locator=locator)
        return element.text
    
    # 判断单个元素是否存在并长时间可见
    def is_element_existed(self, locator):

        try:
            self.find_element(locator=locator)
            return True
        except:
            return False

    # 判断多个元素是否存在并长时间可见
    def is_elements_existed(self, locator):

        try:
            if self.find_elements(locator=locator).__len__() > 1:
                return True
        except:
            return False
    
    # 判断元素是否存在过DOM树中
    def is_element_present(self, locator):
        try:
            if self.wait.until(EC.presence_of_element_located(locator=locator)):
                return True
        except:
            return False
        
    def wait_element_disappear(self, locator):
        
        self.wait.until(EC.invisibility_of_element_located(locator=locator))

    # 对界面做截图操作
    def take_screenshot(self, name):
        self.driver.save_screentshot(f'report/screenshot_{name}.png')

class BaseAssert:

    try:
        # 元素判断
        @classmethod
        def define_assert(cls, real_result, expected_result):
            assert real_result == expected_result

    except Exception as error:
        raise error