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
    # 设定为元组，便于维护
    # 页面元素不需要让业务了解，所以要加私有
    __ele_username = (By.ID, "username")
    __ele_acctid = (By.ID, "memberAdd_acctid")
    __ele_phone = (By.ID, "memberAdd_phone")
    __ele_save = (By.CSS_SELECTOR, ".js_btn_save")
    __ele_save_continue = (By.CSS_SELECTOR, ".js_btn_continue")
    __ele_cancel = (By.CSS_SELECTOR, ".js_btn_cancel")
    __ele_menu_index = (By.ID, "menu_index")
    __ele_menu_contacts = (By.ID, "menu_contacts")

    def goto_main(self):
        """
        跳转到企业微信主页面
        :return:
        """
        self.find(self.__ele_menu_index).click()
        return ContactPage(self.driver)

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(self.__ele_menu_contacts).click()
        return ContactPage(self.driver)

    def add_cancel(self):
        """
        取消添加并返回通讯录页面
        :return:
        """
        self.find(self.__ele_cancel).click()
        return ContactPage(self.driver)

    def add_member(self, username, acctid, phone):
        """
        添加成员并保存返回通讯录页面
        :return:
        """
        self.find(self.__ele_username).send_keys(username)
        self.find(self.__ele_acctid).send_keys(acctid)
        self.find(self.__ele_phone).send_keys(phone)
        self.find(self.__ele_save).click()
        # 返回要跳转页面的实例对象
        return ContactPage(self.driver)

    def add_member_fail(self, username, acctid, phone):
        """
        添加成员失败
        :return:
        """
        self.find(self.__ele_username).send_keys(username)
        self.find(self.__ele_acctid).send_keys(acctid)
        self.find(self.__ele_phone).send_keys(phone)
        self.find(self.__ele_save).click()
        time.sleep(1)
        elements = self.driver.find_elements(By.CLASS_NAME, "ww_inputWithTips_tips")
        error_list = []
        for ele in elements:
            error_list.append(ele.text)
        print(error_list)
        # 返回提示元素信息总数据列表
        return error_list

    def add_save_continue(self, username, acctid, phone):
        """
        保存添加成员,并继续添加
        :return:
        """
        self.find(self.__ele_username).send_keys(username)
        self.find(self.__ele_acctid).send_keys(acctid)
        self.find(self.__ele_phone).send_keys(phone)
        self.find(self.__ele_save_continue).click()
        return self
