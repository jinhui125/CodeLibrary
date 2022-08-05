# -*- coding: UTF-8 -*-
import yaml
import os
from appium import webdriver

device_config_info = {'describe_caps': {
    'platformName': 'Android',
    'platformVersion': '',
    'deviceName': '',
    'appPackage': '',
    'appActivity': '',
    'automationName': 'Uiautomator2',
    'chromedriverExecutable': ''
}
}

rootPath = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
filePath = os.path.join(rootPath, "config\device_config.yaml")
chromeDriver = os.path.join(rootPath, "H5_chromeDriver\chromedriver.exe")


def readYaml(path):
    with open(path, "r+", encoding="utf-8") as file:
        device_data = yaml.load(stream=file, Loader=yaml.FullLoader)
        return device_data


def writeYaml(path, content):
    with open(path, "w+", encoding="utf-8") as file:
        yaml.dump(data=content, stream=file)


def deviceParameterSetting(deviceName, appPackage, appActivity):
    device_config_info['describe_caps']['deviceName'] = deviceName
    device_config_info['describe_caps']['appPackage'] = appPackage
    device_config_info['describe_caps']['appActivity'] = appActivity
    device_config_info['describe_caps']['chromedriverExecutable'] = chromeDriver
    platformVersion = os.popen("adb shell getprop ro.build.version.release")
    device_config_info['describe_caps']['platformVersion'] = platformVersion.read().split(".")[0]
    writeYaml(path=filePath, content=device_config_info)
    describe_caps = readYaml(path=filePath)
    return describe_caps['describe_caps']


def deviceConnect(deviceName, appPackage, appActivity):
    caps = deviceParameterSetting(deviceName=deviceName, appPackage=appPackage,
                                  appActivity=appActivity)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=caps)
    driver.implicitly_wait(8)
    return driver
