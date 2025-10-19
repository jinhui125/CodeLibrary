import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 加载浏览器启动
@pytest.fixture(scope='function')
def browser():
    options = Options()
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-infobars')
    driver = webdriver.Chrome(service=Service(executable_path='../chromeDriver_lib/mac-arm64/chromedriver'), options=options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

class TestWebsite:

    @pytest.mark.ui
    def test_homepage_title(self, browser):
        browser.get(r'https://login.zhipin.com/')
        print(browser.title)
        assert 'BOSS' in browser.title

    @pytest.mark.ui
    @pytest.mark.parametrize('search_term', [
        'python', 'pytest', 'selenium'
    ])
    @pytest.mark.skip(reason='跳过此用例')
    def test_search_functionality(self, browser, search_term):

        browser.get('www.baidu.com')
        search_box = browser.find_element(By.NAME, 'q')
        search_box.send_keys(search_term)
        search_box.submit()
        assert search_term in browser.page_source

