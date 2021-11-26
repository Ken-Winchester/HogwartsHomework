# -*- coding:utf-8 -*-
# @time :2021-11-26  14:32
# @Author :Tyz
# @Email :910771232@qq.com
# @file :add_menber_page.py
from WebWeChatPO.page.contact_page import ContactPage


class AddMemberPage:
    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        return ContactPage()

    def add_member(self):
        """
        添加成员
        :return:
        """
        # 返回要跳转页面的实例对象
        return ContactPage()
