# -*- coding:utf-8 -*-
# @time :2021-11-26  14:33
# @Author :Tyz
# @Email :910771232@qq.com
# @file :contact_page.py
from selenium.webdriver.common.by import By
from WebWeChatPO.page.base_page import BasePage


class ContactPage(BasePage):
    __ele_menu_index = (By.ID, "menu_index")

    def goto_mainpage(self):
        """
        跳转到企业微信主页面
        :return:
        """
        self.find(self.__ele_menu_index).click()
        from WebWeChatPO.page.main_page import MainPage
        return MainPage(self.driver)

    def goto_addmember(self):
        pass

    def get_contact_list(self):
        # 获取的是元素列表（姓名列中的所有元素）
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(ele_list)
        name_list = []
        # 遍历列表，通过元素的text属性，提取文本数据信息
        for ele in ele_list:
            name_list.append(ele.text)
        print(name_list)

        return name_list
