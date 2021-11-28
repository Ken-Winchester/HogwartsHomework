# -*- coding:utf-8 -*-
# @time :2021-11-28  19:13
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_toast.py
import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestToast:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "emulator-5555",
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.view.PopupMenu1",
            "automationName": "uiautomator2",
            "noRset": True,
            "skipDeviceInitialization": False,
            "dontStopAppOnReset": False,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        pass

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        # print(self.driver.page_source) 打印页面
        locatora = (MobileBy.XPATH, "//android.widget.Toast[@text='Clicked popup menu item Search']")
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*locatora))
        print(self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text, 'Clicked popup')]").text)
