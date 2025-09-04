from enum import Enum
from selenium.webdriver.common.by import By

class LoginPageElements(Enum):

    # 推荐牛人按钮
    referral_NB_btn = (By.CSS_SELECTOR, 'a[ka="menu-geek-recommend"]')

    # 职位切换按钮
    job_switch_btn = (By.CSS_SELECTOR, '.job-selecter-wrap .ui-dropmenu-label')

    # 职位选择列表
    job_selection_list_btn = (By.CSS_SELECTOR, '.ui-dropmenu-list .job-list')

    # 职位：前端开发工程师按钮
    FED_engineer_btn = (By.CSS_SELECTOR, '.job-list li:nth-child(1)')

    # 职位：电气设计工程师按钮
    ED_engineer_btn = (By.CSS_SELECTOR, '.job-list li:nth-child(2)')

    # 职位：硬件网络工程师按钮
    HN_engineer_btn = (By.CSS_SELECTOR, '.job-list li:nth-child(3)')

    # 职位：悬架工程师按钮
    CS_engineer_btn = (By.CSS_SELECTOR, '.job-list li:nth-child(4)')

    # 职位：内外饰设计工程师按钮
    IAED_engineer_btn = (By.CSS_SELECTOR, '.job-list li:nth-child(5)')

    # 职位：视频标注按钮
    VA_engineer_btn = (By.CSS_SELECTOR, '.job-list li:nth-child(6)')

    # 筛选按钮
    filter_btn = (By.CSS_SELECTOR, '.filter-label')

    # 筛选条件列表确认按钮
    ok_btn = (By.CSS_SELECTOR, '.btns .btn:nth-child(3)')

    # 打招呼按钮
    say_hi_btn = (By.CSS_SELECTOR, '.btn-greet')

    # 候选人卡片按钮
    candidate_card_btn = (By.CSS_SELECTOR, 'candidate-card-wrap')

    # 候选人卡片关键词tag
    candidate_card_key_tag = (By.CSS_SELECTOR, '.tags-wrap .tag-item')
    
    # 候选人简历详情图片
    resume_png = (By.CSS_SELECTOR, 'canvas[id=resume]')

    # 简历详情页关闭按钮
    resume_close_btn = (By.CSS_SELECTOR, '.icon-close')

    # 简历详情页打招呼按钮
    resume_say_hi_btn = (By.CSS_SELECTOR, '.btn-sure-v2')




