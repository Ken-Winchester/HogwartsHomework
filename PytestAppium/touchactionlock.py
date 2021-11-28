# -*- coding:utf-8 -*-
# @time :2021-11-28  13:46
# @Author :Tyz
# @Email :910771232@qq.com
# @file :touchactionlock.py
import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "emulator-5555",
            "appPackage": "cn.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.FlashActivity",
            "automationName": "uiautomator2",
            "noRset": True,
            "skipDeviceInitialization": False,
            "dontStopAppOnReset": False,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        time.sleep(10)
        pass

    def teardown(self):
        self.driver.quit()

    def test_touchaction_unlock(self):
        print("解锁手势密码")
        """
        1.进入手势密码锁
        2.点击设置手势
        3.设置解锁手势
        4.判断继续按钮是否可点击
        """
        # 1&2
        ele1 = self.driver.find_element(AppiumBy.ID, "cn.kmob.screenfingermovelock:id/patternTxt")
        ele1.click()
        action = TouchAction(self.driver)
        x1, x2, x3 = 120, 360, 600
        y1, y2, y3 = 190, 430, 670
        # 3
        time.sleep(3)
        action.press(x = x1, y = y1).move_to(x = x1, y = y2).wait(100).move_to(x = x2, y = y1).wait(100) \
            .move_to(x = x2, y = y2).wait(100).move_to(x = x3, y = y2).wait(100).move_to(x = x2, y = y3) \
            .wait(100).move_to(x = x3, y = y3).wait(100).release().perform()
        el3 = self.driver.find_element(AppiumBy.ID, "cn.kmob.screenfingermovelock:id/btnTwo")
        enabled = el3.get_attribute("enabled")
        if enabled:
            print("首次设置完成，继续按钮可点击")
        else:
            print("首次设置未完成，请重新设置")
