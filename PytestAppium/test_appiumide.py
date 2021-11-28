# -*- coding:utf-8 -*-
# @time :2021-11-27  22:37
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_appiumide.py
import time

from appium import webdriver

desired_caps = {
    "platformName": "android",
    "deviceName": "emulator-5555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "automationName": "uiautomator2",
    "noRset": True,
    "skipDeviceInitialization": False,
    "dontStopAppOnReset": False,
    "unicodeKeyboard": True,
    "resetKeyboard": True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el3.click()
