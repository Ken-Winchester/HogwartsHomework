# -*- coding:utf-8 -*-
# @time :2021-11-26  22:23
# @Author :Tyz
# @Email :910771232@qq.com
# @file :edit_menber_page.py
from selenium.webdriver.common.by import By
from WebWeChatPO.page.base_page import BasePage
from WebWeChatPO.page.member_info_page import MemberInfoPage


class EditMemberPage(BasePage):
    __ele_save = (By.CSS_SELECTOR, ".js_del_member")
    __ele_cancel = (By.CSS_SELECTOR, ".js_del_member")
    __ele_username = (By.ID, "username")

    def edit_memberinfo_save(self, newname):
        # 点击保存
        self.find(self.__ele_username).send_keys(newname)
        self.find(self.__ele_save).click()
        return MemberInfoPage(self.driver)

    def edit_memberinfo_cancel(self):
        # 点击取消
        self.find(self.__ele_cancel).click()
        return MemberInfoPage(self.driver)
