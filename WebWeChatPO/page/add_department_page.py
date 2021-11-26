# -*- coding:utf-8 -*-
# @time :2021-11-27  0:34
# @Author :Tyz
# @Email :910771232@qq.com
# @file :add_department_page.py
from selenium.webdriver.common.by import By
from WebWeChatPO.page.base_page import BasePage
from WebWeChatPO.page.empty_department_page import EmptyDepartmentPage


class AddDepartmentPage(BasePage):
    __ele_department_name = (By.XPATH, "//label[text()='部门名称']/following-sibling::input")
    __ele_department_dropdown = (By.XPATH, "//label[text()='所属部门']/following-sibling::a")
    __ele_parent_department = (By.XPATH, "//label[text()='所属部门']/following-sibling::div//a[text()='纯蕴']")
    __ele_alert_accept = (By.XPATH, "//*[@id='__dialog__MNDialog__']//a[text()='确定']")
    __ele_alert_cancel = (By.XPATH, "//*[@id='__dialog__MNDialog__']//a[text()='取消']")

    def add_department(self, department_name):
        """
        添加部门
        :return:
        """
        # 填写部门名称
        self.find(self.__ele_department_name).send_keys(department_name)
        # 点击下拉框
        self.find(self.__ele_department_dropdown).click()
        # 选择所属部门
        self.find(self.__ele_parent_department).click()
        # 点击确认
        self.find(self.__ele_alert_accept).click()
        return EmptyDepartmentPage(self.driver)

    def add_cancel(self):
        """
        取消添加部门
        :return:
        """
        # 点击取消按钮
        self.find(self.__ele_alert_cancel).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)
