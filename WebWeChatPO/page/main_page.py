# -*- coding:utf-8 -*-
# @time :2021-11-26  14:34
# @Author :Tyz
# @Email :910771232@qq.com
# @file :main_page.py
from selenium.webdriver.common.by import By
from WebWeChatPO.page.base_page import BasePage


class MainPage(BasePage):
    """
    用公共方法代表UI所提供的功能
    """
    __ele_add_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        self.find(self.__ele_add_member).click()
        from WebWeChatPO.page.add_menber_page import AddMemberPage
        # 返回要跳转的实例对象
        return AddMemberPage(self.driver)
