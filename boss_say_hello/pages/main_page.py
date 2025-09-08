import time
from .base_page import BasePage
from .check_element import CheckElement
from utils.helpers import *
from setElement_lib.mainPage_elements import MainPageElements

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.check_element = CheckElement(driver=driver)

    # 点击推荐牛人按钮
    def click_referral_NB_btn(self):
        self.click(locator=MainPageElements.referral_NB_btn.value)

    # 点击职位切换按钮
    def click_job_switch_btn(self):
        self.click(locator=MainPageElements.job_switch_btn.value)

    # 点击职位选择列表按钮，并等待用户填写筛选条件
    def click_job_selection_list_btn(self, select_position_name):
        self.click(locator=MainPageElements.job_selection_list_btn.value)
        self.check_element.check_element_existed(locator=MainPageElements.ok_btn.value, expected_value=True)
        time.sleep(20)
        self.check_element.check_element_existed(locator=MainPageElements.ok_btn.value, expected_value=False)
    
    # 生成指定数量的候选人信息
    def filter_candidate_number(self, candidate_number=15):

        self.check_element.check_elements_existed(locator=MainPageElements.candidate_card_btn.value, expected_value=True)

        if candidate_number // 15 != 1:
            for i in range((candidate_number // 15) - 1):
                self.roll_window_to_bottom_way_two()
                if self.find_elements(locator=MainPageElements.candidate_card_btn.value).__len__() >= candidate_number:
                    break

        self.roll_window_to_top()

    # 给满足简历要求的候选人打招呼
    def handle_candidate_resume_info(self, condition_ls, say_hi_number=100):

        candidate_cards = self.find_elements(locator=MainPageElements.candidate_card_btn.value)

        for i in range(len(candidate_cards)):
            
            if (say_hi_number-1) != 0:
                candidate_name = candidate_cards[0].text
                self.click(locator=candidate_cards[i])
                self.check_element.check_element_existed(locator=MainPageElements.resume_png.value, expected_value=True)
                self.check_element.check_element_existed(locator=MainPageElements.resume_say_hi_btn.value, expected_value=True)
                self.transform_canvas_to_png(element=candidate_cards[0], png_path='../resume_png_lib', candidate_name=candidate_name)
                image_text = OCR_image(image_path=f'../resume_png_lib/{candidate_name}_canvas_image.png')
                with_condition_ls = [ x for x in condition_ls if '&' in x]
                or_condition_ls = [y for y in condition_ls if '&' not in y]

                # 存在与条件和或条件
                if len(with_condition_ls) != 0 and len(or_condition_ls) != 0:
                    
                    matched_result = []
                    tmp_ls = []
                    for with_condition in with_condition_ls:
                        with_condition = [x.strip() for x in with_condition.split('&')]
                        tmp_ls.extend(with_condition)
                    with_matched_result = []
                    for condition in tmp_ls:
                        with_matched_result.append(is_matched_string_list(pattern=f'{condition}', text=image_text))

                    or_matched_result = [is_matched_string_list(pattern='|'.join(or_condition_ls), text=image_text)]
                    matched_result.extend(with_matched_result)
                    matched_result.extend(or_matched_result)
                    if len(set(matched_result)) == 1 and set(matched_result)[0] == True:
                        self.click(MainPageElements.resume_say_hi_btn.value)
                    else:
                        self.click(MainPageElements.resume_close_btn.value)
                        
                # 只存在与条件
                elif len(with_condition_ls) != 0 and len(or_condition_ls) == 0:
                    matched_result = []
                    tmp_ls = []
                    for with_condition in with_condition_ls:
                        with_condition = [x.strip() for x in with_condition.split('&')]
                        tmp_ls.extend(with_condition)
                    with_matched_result = []
                    for condition in tmp_ls:
                        with_matched_result.append(is_matched_string_list(pattern=f'{condition}', text=image_text))
                    if len(set(matched_result)) == 1 and set(matched_result)[0] == True:
                        self.click(MainPageElements.resume_say_hi_btn.value)
                    else:
                        self.click(MainPageElements.resume_close_btn.value)

                # 只存在或条件
                elif len(with_condition_ls) == 0 and len(or_condition_ls) != 0:
                    or_matched_result = [is_matched_string_list(pattern='|'.join(or_condition_ls), text=image_text)]
                    if or_matched_result[0]:
                        self.click(MainPageElements.resume_say_hi_btn.value)
                    else:
                        self.click(MainPageElements.resume_close_btn.value)
                else:
                    self.click(MainPageElements.resume_close_btn.value)
            else:
                break
        print(f'{say_hi_number}个招呼打完了，累死我了')

            


            

        



        

        


        

    