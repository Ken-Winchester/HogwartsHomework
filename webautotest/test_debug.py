# -*- coding:utf-8 -*-
# @time :2021-11-02  13:00
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_debug.py
import time

import pytest
import selenium
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


# 复用只支持chrome浏览器  目的（包括但不限）：验证部分代码行是否正确执行
# 需要先使用命令行启动浏览器:chrome --remote-debugging-port=9898  再到页面定位需要操作的元素
class TestDebug:
    @pytest.fixture
    def get_cookies(self):
        self.driver = webdriver.Chrome()
        hogwartscookies = self.driver.get_cookies()
        return hogwartscookies

    # 加了标签后不能直接当作用例运行了，只能当作普通函数,所以加标签时要注意区分
    # @pytest.fixture
    def test_debug(self):
        # 连接当前页面
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9898"
        self.driver = webdriver.Chrome(options = opt)
        self.driver.implicitly_wait(3)
        # 对当前页面元素进行操作
        # self.driver.find_element(By.ID, "kw").send_keys("12345")
        # self.driver.find_element(By.ID, "su").click()
        hogwartscookies = self.driver.get_cookies()  # 此处获取的cookie是登录https://ceshiren.com后的cookie
        with open("./hogwartscookies.yaml", "w", encoding = "utf-8") as f:
            yaml.dump(hogwartscookies, f)

    # 利用cookie登录
    def test_cookies(self, get_cookies):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://ceshiren.com/t/topic/14761/13")
        time.sleep(3)
        print(get_cookies)
        for cookie in get_cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://ceshiren.com/t/topic/14761/13")
        time.sleep(3)
        self.driver.quit()
