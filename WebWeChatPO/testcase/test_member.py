# -*- coding:utf-8 -*-
# @time :2021-11-26  14:51
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_member.py
import pytest
from WebWeChatPO.page.main_page import MainPage


class TestMember:
    """
    编写测试用例
    """

    def setup(self):
        self.main_page = MainPage()

    def teardown(self):
        self.main_page.quit()

    # 实现测试数据和页面对象分离
    @pytest.mark.parametrize("username, acctid, phone",
                             [("aaa", "0001", "13344445555"), ("eeeee", "00032", "13344445551")])
    def test_add_member(self, username, acctid, phone):
        #      1.跳转到添加成员页面  2.添加成员操作  3.获取成员列表
        name_list = self.main_page.goto_add_member().add_member(username, acctid, phone).get_contact_list()
        assert username in name_list

    @pytest.mark.parametrize("username, acctid, phone", [("bbb", "0002", "13344445555")])
    def test_add_member_fail(self, username, acctid, phone):
        data_list = self.main_page.goto_add_member().add_member_fail(username, acctid, phone)
        # 寻找所有的错误元素信息，如果不为空，则返回
        err = [i for i in data_list if i is not ""]
        assert "占有" in err[0]

    @pytest.mark.parametrize("oldname, newname", [("eeeee", "bbb")])
    def test_edit_member_name(self, oldname, newname):
        # 传入要编辑的旧姓名和新姓名
        name_list = self.main_page.goto_contact().get_contact_list()
        # 判断人员是否存在
        if oldname in name_list:
            if newname not in name_list:
                #  1.进入通讯录页面  2.进入成员信息页面  3.进入编辑成员页面  4.编辑成员姓名并保存  5.返回通讯录页面  6.获取成员列表
                newname_list = self.main_page.goto_contact().goto_member_info(
                    oldname).goto_edit_memberinfo().edit_memberinfo_save(newname).goback_contact()
                # .get_contact_list()
            else:
                print("新姓名已存在")
                return False
        else:
            # 如果人员不存在，则返回提示
            print("人员不存在")
            return False
        print(newname_list)
        # assert newname in newname_list

    @pytest.mark.parametrize("username", ["bbb"])
    def test_memberinfo_delete_member(self, username):
        # 传入要删除的人员名称
        name_list = self.main_page.goto_contact().get_contact_list()
        # 判断人员是否存在
        if username in name_list:
            #  1.进入通讯录  2.进入成员信息  3.删除成员并返回通讯录  4.获取成员列表
            name_list = self.main_page.goto_contact().goto_member_info(username).delete_member().get_contact_list()
        else:
            # 如果人员不存在，则返回提示
            print("人员不存在")
            return False

        assert username not in name_list

    @pytest.mark.parametrize("username", ["aaa"])
    def test_contact_delete_member(self, username):
        # 传入要删除的人员名称
        name_list = self.main_page.goto_contact().get_contact_list()
        # 判断人员是否存在
        if username in name_list:
            #  1.进入通讯录  2.选择成员并删除  3.获取成员列表
            newname_list = self.main_page.goto_contact().select_delete_member(username).get_contact_list()
        else:
            # 如果人员不存在，则返回提示
            print("人员不存在")
            return False

        assert username not in newname_list
