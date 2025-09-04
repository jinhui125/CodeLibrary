import pytest
from utils.helpers import load_yaml_file
from conftest import login_page

test_data = load_yaml_file(file_path='../test_data/test_data.yaml')

class TestLogin:
    
    def test_user_login(self, login_page):
        phone_number = test_data['phone-numbers'][0]['phone-number-1']
        # auth_code = input('请输入手机验证码：').strip
        login_page.open()
        login_page.user_login(phone_number=phone_number, auth_code='123456')