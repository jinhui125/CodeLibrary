# -*- coding: UTF-8 -*-
import os
import unittest
from HTMLTestRunner import HTMLTestRunner


rootPath = os.path.abspath(os.path.dirname(__file__))
testcasesPath = os.path.join(rootPath, "testcase\jumei_APP\login_testcases")

# runner = unittest.TextTestRunner()
report_dir = os.path.abspath(os.path.dirname(__file__))
report_file = os.path.join(report_dir, "testreport\html_report.html")

with open(report_file, "w", encoding="utf-8") as rf:
    discover = unittest.defaultTestLoader.discover(start_dir=testcasesPath, pattern="wrong_account_login.py")

    runner = HTMLTestRunner(title='聚美APP测试', description="登录账号测试", stream=rf)
    runner.run(discover)

