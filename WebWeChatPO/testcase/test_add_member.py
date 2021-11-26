# -*- coding:utf-8 -*-
# @time :2021-11-26  14:51
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_add_member.py
import pytest
from selenium import webdriver
from WebWeChatPO.page.contact_page import ContactPage
from WebWeChatPO.page.main_page import MainPage


class TestAddMember:
    """
    编写测试用例
    """

    def setup(self):
        self.main_page = MainPage()

    def teardown(self):
        self.main_page.quit()

    # 实现测试数据和页面对象分离
    @pytest.mark.parametrize("username, acctid, phone", [("aaa", "0001", "13344445555")])
    def test_add_member(self, username, acctid, phone):
        #      1.跳转到添加成员页面  2.添加成员操作  3.获取成员列表
        name_list = self.main_page.goto_addmember().add_member(username, acctid, phone).get_contact_list()
        assert username in name_list

    @pytest.mark.parametrize("username, acctid, phone", [("bbb", "0002", "13344445555")])
    def test_add_member_fail(self, username, acctid, phone):
        #      1.跳转到添加成员页面  2.添加成员操作  3.获取成员列表
        data_list = self.main_page.goto_addmember().add_member_fail(username, acctid, phone)
        # 寻找所有的错误元素信息，如果不为空，则返回
        err = [i for i in data_list if i is not ""]
        assert "占有" in err[0]
