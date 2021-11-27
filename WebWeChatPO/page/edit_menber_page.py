# -*- coding:utf-8 -*-
# @time :2021-11-26  22:23
# @Author :Tyz
# @Email :910771232@qq.com
# @file :edit_menber_page.py
from selenium.webdriver.common.by import By
from WebWeChatPO.page.base_page import BasePage


class EditMemberPage(BasePage):
    __ele_save = (By.CSS_SELECTOR, ".js_save")
    __ele_cancel = (By.CSS_SELECTOR, ".js_cancel")
    __ele_username = (By.ID, "username")

    def edit_memberinfo_save(self, newname):
        self.driver.implicitly_wait(3)
        # 点击保存
        self.find(self.__ele_username).clear()
        self.find(self.__ele_username).send_keys(newname)
        self.find(self.__ele_save).click()
        from WebWeChatPO.page.member_info_page import MemberInfoPage
        return MemberInfoPage(self.driver)

    def edit_memberinfo_cancel(self):
        self.driver.implicitly_wait(3)
        # 点击取消
        self.find(self.__ele_cancel).click()
        from WebWeChatPO.page.member_info_page import MemberInfoPage
        return MemberInfoPage(self.driver)
