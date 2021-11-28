# -*- coding:utf-8 -*-
# @time :2021-11-27  23:34
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_locate.py
import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class TestLocate:
    def setup(self):
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
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        pass

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        """
        1. 打开雪球app
        2.点击搜索输入框
        3.向搜索输入框输入 “阿里巴巴”
        4.在搜索结果中选择 “阿里巴巴”
        5.获取这只阿里巴巴的股价，并判断这只股价的价格
        
        """
        el1 = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        el3 = self.driver.find_element(AppiumBy.XPATH,
                                       "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        el3.click()
        time.sleep(3)
        el4 = float(
            self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/current_price']").text)

        assert el4 > 130

    def test_attribute(self):
        """
        打开雪球，定位首页搜索框
        判断搜索框是否可用，并查看搜索框的name属性
        打印搜索框这个元素的左上角坐标和他的宽高
        向搜索框输入alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印“搜索成功”并点击
        如果不可见，打印“搜索失败”
        :return:
        """
        el1 = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search")
        ele_search = el1.is_enabled()
        if ele_search:
            print("搜索框可用")
            name = el1.get_attribute("name")
            print(name)
            print(el1.location)
            print(el1.size)

            el1.click()
            el2 = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text")
            el2.send_keys("阿里巴巴")
            el3 = self.driver.find_element(AppiumBy.XPATH,
                                           "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            alibaba = el3.is_displayed()
            if alibaba:
                print("搜索成功")
                el3.click()
            else:
                print("搜索失败")
        else:
            print("搜索框不可用")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect["width"]
        height = window_rect["height"]
        x_start = width / 2
        y_start = int(height * 0.8)
        y_end = int(height * 0.2)
        action.press(x = x_start, y = y_start).move_to(x = x_start, y = y_end).release().perform()

# if __name__ == '__main__':
#     pytest.main()
