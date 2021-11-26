# -*- coding:utf-8 -*-
# @time :2021-11-27  0:48
# @Author :Tyz
# @Email :910771232@qq.com
# @file :add_sub_department_page.py
from selenium.webdriver.common.by import By

from WebWeChatPO.page.base_page import BasePage


class AddSubDepartmentPage(BasePage):
    __ele_sub_department_name = (By.XPATH, "//label[text()='部门名称']/following-sibling::input")
    __ele_alert_accept = (By.XPATH, "//*[@id='__dialog__MNDialog__']//a[text()='确定']")
    __ele_alert_cancel = (By.XPATH, "//*[@id='__dialog__MNDialog__']//a[text()='取消']")

    def add_sub_department(self, department_name):
        """
        添加部门
        :return:
        """
        # 填写子部门名称
        self.find(self.__ele_sub_department_name).send_keys(department_name)
        # 点击确认
        self.find(self.__ele_alert_accept).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def add_cancel(self):
        """
        取消添加部门
        :return:
        """
        # 点击取消按钮
        self.find(self.__ele_alert_cancel).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)
