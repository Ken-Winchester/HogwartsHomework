# -*- coding:utf-8 -*-
# @time :2021-11-26  11:39
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_alert.py
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAlert:
    def test_alert(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.driver.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")

        drag = self.driver.find_element(By.ID, "draggable")
        drop = self.driver.find_element(By.ID, "droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

        print("点击 alert 确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submitBTN").click()
        time.sleep(2)
