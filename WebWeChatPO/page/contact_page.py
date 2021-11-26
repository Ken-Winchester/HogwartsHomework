# -*- coding:utf-8 -*-
# @time :2021-11-26  14:33
# @Author :Tyz
# @Email :910771232@qq.com
# @file :contact_page.py
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from WebWeChatPO.page.base_page import BasePage


class ContactPage(BasePage):
    __ele_menu_index = (By.ID, "menu_index")
    __ele_add_member = (By.XPATH, "//*[@class='ww_operationBar']/a[text()='添加成员']")
    __ele_dropdown = (By.XPATH, "//*[@class='ww_operationBar']//div[text()='批量导入/导出']")
    __ele_upload_file = (By.XPATH, "//*[@class='ww_operationBar']//a[text()='文件导入']")
    __ele_del_member = (By.XPATH, "//*[@class='ww_operationBar']/a[text()='删除']")
    __ele_add = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    __ele_add_department = (By.CSS_SELECTOR, ".js_create_party")
    __ele_add_sub_department = (By.CSS_SELECTOR, ".js_add_sub_party")

    def goto_main(self):
        """
        跳转到企业微信主页面
        :return:
        """
        self.find(self.__ele_menu_index).click()
        from WebWeChatPO.page.main_page import MainPage
        return MainPage(self.driver)

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        self.find(self.__ele_add_member).click()
        from WebWeChatPO.page.add_menber_page import AddMemberPage
        return AddMemberPage(self.driver)

    def goto_member_info(self, username):
        """
        跳转到成员信息页面
        :return:
        """
        self.find(By.XPATH, f"//*[text()='{username}']").click()
        from WebWeChatPO.page.member_info_page import MemberInfoPage
        return MemberInfoPage(self.driver)

    def goto_add_department(self):
        """
        跳转到添加部门页面
        :return:
        """
        self.find(self.__ele_add).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(*self.__ele_add_department))
        self.find(self.__ele_add_department).click()
        from WebWeChatPO.page.add_department_page import AddDepartmentPage
        return AddDepartmentPage(self.driver)

    def goto_add_sub_department(self):
        """
        跳转到添加子部门页面
        :return:
        """
        self.find(self.__ele_add_sub_department).click()
        from WebWeChatPO.page.add_sub_department_page import AddSubDepartmentPage
        return AddSubDepartmentPage(self.driver)

    def goto_upload_file(self):
        """
        跳转到导入通讯录页面
        :return:
        """
        self.find(self.__ele_dropdown).click()
        self.find(self.__ele_upload_file).click()
        from WebWeChatPO.page.upload_file_page import UploadFilePage
        return UploadFilePage(self.driver)

    def get_contact_list(self):
        """
        获取成员列表
        :return:
        """
        # 获取的是元素列表（姓名列中的所有元素）
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(ele_list)
        name_list = []
        # 遍历列表，通过元素的text属性，提取文本数据信息
        for ele in ele_list:
            name_list.append(ele.text)
        print(name_list)

        return name_list

    def select_delete_member(self, username):
        """
        选择成员并删除
        :param username:
        :return:
        """
        self.find(By.XPATH, f"//*[text()='{username}']/ancestor::td/preceding-sibling::td").click()
        self.find(self.__ele_del_member).click()
        return self
