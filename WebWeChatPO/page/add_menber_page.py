# -*- coding:utf-8 -*-
# @time :2021-11-26  14:32
# @Author :Tyz
# @Email :910771232@qq.com
# @file :add_menber_page.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from WebWeChatPO.page.base_page import BasePage

from WebWeChatPO.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        return ContactPage(self.driver)

    def add_member(self):
        """
        添加成员
        :return:
        """

        self.driver = webdriver.Chrome()
        self.driver.find_element(By.ID, "username").send_keys("aaa")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("00001")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13546786454")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        time.sleep(20)

        # 返回要跳转页面的实例对象
        return ContactPage(self.driver)
