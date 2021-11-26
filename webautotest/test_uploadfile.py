# -*- coding:utf-8 -*-
# @time :2021-11-26  11:26
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_uploadfile.py
# from selenium.webdriver.selenium_frame_window.base import Base
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFile:
    def test_file_upload(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://image.baidu.com")
        self.driver.find_element(By.ID, "stfile").send_keys("C:/Users/Administrator/Desktop/bz.png")
        time.sleep(3)
