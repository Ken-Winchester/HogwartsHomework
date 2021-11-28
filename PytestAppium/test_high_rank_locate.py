# -*- coding:utf-8 -*-
# @time :2021-11-28  15:09
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_high_rank_locate.py
import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHighRankLocate:
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

    def UiautomatorSelector(self):
        """
        # 定位UiSelector
        # 组合定位id&text;class&text
        id_text = 'new UiSelector().resourceId("com.xueqiu.android:id/button_next").text("登录")'
        login_button = self.driver.find_element_by_android_uiautomator(id_text)
        # 父子定位childSelector：
        'new UiSelector().childSelector(resourceId(""))'
        # 兄弟定位fromParent：
        'new UiSelector().fromParent(text(""))'
        ...
        # 滚动查找元素
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("查找的文本").instance(0));'

        :return:
        """
        pass

    def test_locate(self):
        el1 = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        el3 = self.driver.find_element(AppiumBy.XPATH,
                                       "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        el3.click()
        time.sleep(3)
        el4 = float(self.driver.find_element(AppiumBy.XPATH,
                                             "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']/../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(el4)
        stock = self.driver.find_element(AppiumBy.XPATH,
                                         "//*[@resource-id='com.xueqiu.android:id/title_container']/android.widget.TextView[@text='股票']")
        stock.click()

    def test_myinfo(self):
        """
        1.点击“我的”按钮，进入个人信息页面
        2.点击登录，进入登陆页面
        3.输入用户名和密码
        4.点击登录
        :return:
        """
        # 提示"Please use 'find_element' with 'AppiumBy.ANDROID_UIAUTOMATOR' instead."但是需要版本兼容才能用
        # ele_mine = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的")')
        ele_mine = self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")')
        ele_mine.click()
        # textContains()方法可能在当前jdk版本中无法使用
        # login_link = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码")')
        login_link = self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")')
        login_link.click()
        username = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("请输入手机号或邮箱")')
        username.send_keys("123")
        password = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")')
        password.send_keys("456789")
        # 组合定位id&text;class&text
        id_text = 'new UiSelector().resourceId("com.xueqiu.android:id/button_next").text("登录")'
        login_button = self.driver.find_element_by_android_uiautomator(id_text)
        login_button.click()
        tips = self.driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup")
        alert = tips.is_displayed()
        assert alert
        # is True

    def test_scroll(self):
        # 执行时出现上下来回滑动，没有一直向下划屏
        # hot_post = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("扬帆-007").instance(0));')
        # hot_post.click()
        pass

    def test_wait(self):
        # 显示等待
        ele = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.driver.find_element_by_android_uiautomator('new UiSelector().text("热门")')))
        locatora = (MobileBy.ID, "com.xueqiu.android:id/tv_search")
        # lambda表达式
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*locatora))
        print(ele.text)
