# -*- coding:utf-8 -*-
# @time :2021-11-01  15:53
# @Author :Tyz
# @Email :910771232@qq.com
# @file :browserselect.py
from selenium import webdriver
import os


class Base:
    def setup(self):
        browser = os.getenv("browser")
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "headless":
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
