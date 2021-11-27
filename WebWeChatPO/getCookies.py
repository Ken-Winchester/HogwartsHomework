# -*- coding:utf-8 -*-
# @time :2021-11-26  13:12
# @Author :Tyz
# @Email :910771232@qq.com
# @file :getCookies.py
import time
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGetCookies:
    # 加了标签后不能直接当作用例运行了，只能当作普通函数,所以加标签时要注意区分
    # @pytest.fixture
    def test_debug(self):
        # 连接当前页面
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9898"
        self.driver = webdriver.Chrome(options = opt)
        self.driver.implicitly_wait(3)

        wechat_cookies = self.driver.get_cookies()  # 此处获取的cookie是登录企业微信后的cookie
        with open("wechat_cookies.yaml", "w", encoding = "utf-8") as f:
            yaml.dump(wechat_cookies, f)
        print(wechat_cookies)

    # 利用cookie登录
    def test_cookies(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        time.sleep(3)
        with open("wechat_cookies.yaml", encoding = "utf-8") as f:
            yaml_data = yaml.safe_load(f)
        print(yaml_data)
        for cookie in yaml_data:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.XPATH, "//*[text()='通讯录']")
        time.sleep(5)
        self.driver.quit()
