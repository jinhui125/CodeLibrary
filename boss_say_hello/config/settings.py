import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service

base_url = r'https://login.zhipin.com/' # 基础网址链接
BROWSER = 'chrome'  # 浏览器类型 可选: chrome, firefox, edge
HEADLESS = False    # 无头模式
IMPLICIT_WAIT = 10  # 隐式等待时间（单位：秒）
EXPLICIT_WAIT = 10  # 显示等待时间（单位：秒）

def chrome_options():
    """
        浏览器参数配置函数
    """

    options = Options()
    if HEADLESS:
        options.add_argument('--headless')  # 无头模式，不显示GUI
    options.add_argument('--no-sandbox')    # 禁用沙盒（在CI环境中常用）
    options.add_argument('--disable-dev-shm-usage') # 解决内存共享问题
    options.add_argument('--window-size=1920,1080') # 设置窗口大小为1920*1080

    return options

