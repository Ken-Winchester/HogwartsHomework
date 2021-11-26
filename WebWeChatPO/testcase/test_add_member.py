# -*- coding:utf-8 -*-
# @time :2021-11-26  14:51
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_add_member.py
from WebWeChatPO.page.main_page import MainPage


class TestAddMember:
    """
    编写测试用例
    """

    def test_add_member(self):
        main_page = MainPage()
        #      1.跳转到添加成员页面  2.添加成员操作  3.获取成员列表
        main_page.goto_addmember().add_member().get_contact_list()
