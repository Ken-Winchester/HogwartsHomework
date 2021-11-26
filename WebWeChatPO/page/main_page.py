# -*- coding:utf-8 -*-
# @time :2021-11-26  14:34
# @Author :Tyz
# @Email :910771232@qq.com
# @file :main_page.py
from WebWeChatPO.page.add_menber_page import AddMemberPage


class MainPage:
    """
    用公共方法代表UI所提供的功能
    """

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        pass

    def goto_addmember(self):
        """
        跳转到添加成员页面
        :return:
        """
        return AddMemberPage()
