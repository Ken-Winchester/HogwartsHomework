# -*- coding:utf-8 -*-
# @time :2021-11-27  3:30
# @Author :Tyz
# @Email :910771232@qq.com
# @file :download_file_page.py
from selenium.webdriver.common.by import By
from WebWeChatPO.page.base_page import BasePage


class DownloadFilePage(BasePage):
    __ele_back = (By.CSS_SELECTOR, ".ww_btn_Back")
    __ele_upload_input = (By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask")
    __ele_confirm_upload = (By.ID, "ww_fileImporter_submit")
    __ele_complate = (By.XPATH, "//a[contains(text(),'完成')]")
    __ele_download_demo = (By.CSS_SELECTOR, ".ww_fileImporter_header_download")

    def goback_contact(self):
        self.find(self.__ele_back).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def upload_file(self):
        self.find(self.__ele_upload_input).send_keys("../data/uploadfilecontacts.xlsx")
        self.find(self.__ele_confirm_upload).click()
        self.find(self.__ele_complate).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def download_upload_file(self):
        self.find(self.__ele_download_demo).click()
        # 下载文件到上传过程

        self.find(self.__ele_upload_input).send_keys("../data/uploadfilecontacts.xlsx")
        self.find(self.__ele_confirm_upload).click()
        self.find(self.__ele_complate).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)
