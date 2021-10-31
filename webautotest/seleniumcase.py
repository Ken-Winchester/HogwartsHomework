# -*- coding:utf-8 -*-
# @time :2021-10-31  19:06
# @Author :Tyz
# @Email :910771232@qq.com
# @file :seleniumcase.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class hogwarts:
    def steup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        time.sleep(3)
        self.driver.find_element(By.ID, "su").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 - 主页")
