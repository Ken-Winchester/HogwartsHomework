# -*- coding:utf-8 -*-
# @time :2021-11-26  22:02
# @Author :Tyz
# @Email :910771232@qq.com
# @file :member_info_page.py
import time
from selenium.webdriver.common.by import By
from WebWeChatPO.page.base_page import BasePage


class MemberInfoPage(BasePage):
    __ele_back = (By.CSS_SELECTOR, ".js_back")
    __ele_edit = (By.CSS_SELECTOR, ".js_edit")
    __ele_disable_enable = (By.CSS_SELECTOR, ".js_disable")
    __ele_delete = (By.CSS_SELECTOR, ".js_del_member")
    __ele_alert_accept = (By.XPATH, "//*[@id='__dialog__MNDialog__']//a[text()='确定']")
    __ele_del_accept = (By.XPATH, "//*[@id='__dialog__MNDialog__']//a[text()='确认']")

    def disable_enable_member(self):
        """
        禁用/启用成员
        :return:
        """
        self.driver.implicitly_wait(3)
        ele = self.find(self.__ele_disable_enable).text
        dis = "禁用"
        if ele is not dis:
            # 点击启用按钮
            self.find(self.__ele_disable_enable).click()
        else:
            # 点击禁用按钮
            self.find(self.__ele_disable_enable).click()
            # 确认禁用
            self.find(self.__ele_alert_accept).click()
        return self

    def goback_contact(self):
        """
        返回到通讯录页面
        :return:
        """
        self.driver.implicitly_wait(3)
        # 点击返回按钮，回到通讯录
        self.find(self.__ele_back).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def delete_member(self):
        """
        删除成员并返回通讯录页面
        :return:
        """
        self.driver.implicitly_wait(3)
        # 点击删除按钮
        self.find(self.__ele_delete).click()
        time.sleep(2)
        # 确认删除
        self.find(self.__ele_del_accept).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def goto_edit_memberinfo(self):
        """
        进入编辑成员页面
        :return:
        """
        self.driver.implicitly_wait(3)
        time.sleep(3)
        # 点击编辑按钮
        self.find(self.__ele_edit).click()
        from WebWeChatPO.page.edit_menber_page import EditMemberPage
        return EditMemberPage(self.driver)
