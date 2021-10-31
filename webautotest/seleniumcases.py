# -*- coding:utf-8 -*-
# @time :2021-10-31  20:27
# @Author :Tyz
# @Email :910771232@qq.com
# @file :seleniumcases.py
import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSearch:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        # 设置全局的隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        # 强制等待
        # time.sleep(3)
        self.driver.find_element(By.ID, "su").click()
        self.driver.find_element(By.LINK_TEXT, "关于我们 - 霍格沃兹测试学院").click()
        # 获取新窗口的句柄
        windows = self.driver.window_handles
        # 切换到新窗口
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.XPATH, "//div[@id='content']//a[.='学员社区']").click()
        self.driver.find_element(By.XPATH, "//*[@title='所有分类']").click()

        # 定义函数判断返回页面符合要求的元素个数
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, "//*[@class='table-heading']")) >= 1

        # selenium的显示等待，将函数中的self.driver传给了method参数，注意传参和调用的区别是否带()
        WebDriverWait(self.driver, 5).until(wait)

        # 或者直接使用selenium内置条件
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//*[@class='table-heading']")))

        self.driver.find_element(By.XPATH, "//*[@title='过去一年、一个月、一周或一天中最活跃的话题']").click()
