import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config.settings import BROWSER, HEADLESS, IMPLICIT_WAIT, chrome_options

@pytest.fixture(scope='function')
def driver():

    if BROWSER.lower() == 'chrome':
        options = chrome_options()
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver = webdriver.Chrome(service=ChromeService(executable_path='../chromeDriver_lib/chromedriver.exe'), options=options)
        # driver = webdriver.Chrome(options=options)

    elif BROWSER.lower() == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif BROWSER.lower() == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f'不支持的浏览器：{BROWSER}')
    
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture(scope='function')
def login_page(driver):
    from pages.login_page import LoginPage
    return LoginPage(driver=driver)

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makeReport(item, call):
#     outcome = yield
#     report = outcome.get_result()

#     if report.when == 'call' and report.failed:
#         # 获取driver fixture
#         driver_fixture = item.funcargs.get('driver')
#         if driver_fixture:
#             # 截图保存
#             screenshot_name = f"{item.name}_{report.when}.png"
#             driver_fixture.save_screenshot(f"reports/{screenshot_name}")
#             report.extra = [pytest_html.extras.image(f"reports/{screenshot_name}")]

# 多个包装器的执行顺序
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)   # 最先执行前置代码
# def wrapper1():
#     print('Wrapper1 before')
#     outcome = yield
#     print('Wrapper1 after')

# @pytest.hookimpl(hookwrapper=True)  # 中间执行
# def wrapper2():
#     print('Wrapper2 before')
#     outcome = yield
#     print('Wrapper2 after')

# @pytest.hookimpl(trylast=True, hookwrapper=True)  # 最后执行前置代码
# def wrapper3():
#     print('Wrapper3 before')
#     outcome = yield
#     print('Wrapper3 after')

if __name__ == '__main__':
    pass