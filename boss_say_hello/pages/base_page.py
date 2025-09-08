import time
import base64
from io import BytesIO
from PIL import Image
from selenium import webdriver
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

    # 滑动屏幕底部【方式一】
    def roll_window_to_bottom_way_one(self, stop_length, step_length=500):
        """Selenium 滚动当前页面，向下滑动
        :param browser: selenium的webdriver
        :param stop_length: 最大滑动距离（像素）
        :param step_length: 每次滑动的距离（像素）
        """

        original_top = 0
        while True:
            if stop_length:
                if stop_length - step_length < 0:
                    self.driver.execute_script(f'window.scrollBy(0, {stop_length})')
                    break
                stop_length -= step_length
            self.driver.execute_script(f'window.scrollBy(0, {step_length})')
            time.sleep(0.5)

            check_height = self.driver.execute_script(
                'return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;'
            )
            if check_height == original_top:
                break

            original_top = check_height

    # 滑动屏幕底部【方式二】
    def roll_window_to_bottom_way_two(self):

        self.driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')

    # 滑动顶部
    def roll_window_to_top(self):
        
        self.driver.execute_script('window.scrollTo(0, 0)')

    def transform_canvas_to_png(self, element, png_path, candidate_name):
        
        canvas_data = self.driver.execute_script('return arguments[0].toDataURL("image/png").substring(21);', element)
        image_data = base64.b64decode(canvas_data)
        # with open(file=f'{png_path}//{candidate_name}_canvas_image.png', mode='wb') as fb:
        #     fb.write(image_data)

        # 创建BytesIO对象并从内存中读取图像
        image_buffer = BytesIO(image_data)
        image = Image.open(image_buffer)

        if image.mode not in ['RGB', 'RGBA']:
            image = image.convert('RGB')

        image.save(f'{png_path}//{candidate_name}_canvas_image.png', 'PNG')

        # return image
    
class BaseAssert:

    try:
        # 元素判断
        @classmethod
        def define_assert(cls, real_result, expected_result):
            assert real_result == expected_result

    except Exception as error:
        raise error