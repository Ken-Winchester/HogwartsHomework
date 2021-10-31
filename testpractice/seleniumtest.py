# -*- coding:utf-8 -*-
# @time :2021-10-31  15:50
# @Author :Tyz
# @Email :910771232@qq.com
# @file :seleniumtest.py
import selenium
from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
