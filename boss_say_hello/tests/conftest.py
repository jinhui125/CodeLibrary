import pytest

@pytest.fixture(scope='class')
def setup_data():
    """在每个测试前执行"""
    data = {'name': 'John', 'age': 30}
    print('Setup data')
    yield data
    print('Teardown')

def test_user_data(setup_data):
    assert setup_data['name'] == 'John'
    assert setup_data['age'] == 30

@pytest.mark.parametrize('input, expected', [
        (1, 2),
        (2, 4),
        (3, 6)
])
def test_double(input, expected):
    assert input * 2 == expected

@pytest.mark.parametrize('a, b, expected', [
        (1, 2, 3),
        (4, 5, 9),
        (10, 20, 30)
])
def test_addition(a, b, expected):
    assert a + b == expected

@pytest.mark.parametrize('browser', ["chrome", "firefox", "edge"])
class TestBrowserCompatibility:
    def test_opn_url(self, browser):
        assert browser in ["chrome", "firefox", "edge"]
    def test_browser_name(self, browser):
        assert len(browser) > 0

@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(2)
    assert True

@pytest.mark.integration
def test_integration():
    assert True

@pytest.mark.ui
def test_ui_functionality():
    assert True

@pytest.mark.skip(reason='功能尚未实现')
def test_unimplemented():
    assert False

@pytest.mark.skipif(1 == 1, reason='总是跳过')
def test_always_skip():
    assert False

@pytest.mark.xfail(reason='已知问题')
def test_know_issuse():
    assert False
