# -*- coding:utf-8 -*-
# @time :2021-11-02  15:58
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_cookie.py
import yaml
from selenium import webdriver
import time


class TestCookie:
    def test_cookies2(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://ceshiren.com/t/topic/14761/13")
        time.sleep(3)
        with open("./hogwartscookies.yaml", encoding = "utf-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://ceshiren.com/t/topic/14761/13")
        time.sleep(3)
        self.driver.quit()
