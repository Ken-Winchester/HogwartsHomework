# -*- coding:utf-8 -*-
# @time :2021-11-27  1:18
# @Author :Tyz
# @Email :910771232@qq.com
# @file :upload_file_page.py
from selenium.webdriver.common.by import By
from WebWeChatPO.page.base_page import BasePage



class UploadFilePage(BasePage):
    __ele_back = (By.CSS_SELECTOR, ".ww_btn_Back")
    __ele_download_file = (By.CSS_SELECTOR, ".js_go_template_import")
    __ele_upload_label = (By.CSS_SELECTOR, ".js_upload_label")
    __ele_upload_input = (By.CSS_SELECTOR, ".ww_fileInputWrap")
    __ele_confirm_upload = (By.ID, "submit_csv")
    __ele_reload_contact = (By.ID, "reloadContact")

    def goback_contact(self):
        self.find(self.__ele_back).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def goto_download_file(self):
        self.find(self.__ele_download_file).click()
        from WebWeChatPO.page.download_file_page import DownloadFilePage
        return DownloadFilePage(self.driver)

    def upload_file(self):
        self.find(self.__ele_upload_input).send_keys("../data/uploadfilecontacts.xlsx")
        self.find(self.__ele_confirm_upload).click()
        self.find(self.__ele_reload_contact).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def reupload_file(self):
        # 上传文件操作

        self.find(self.__ele_upload_label).click()
        self.find(self.__ele_confirm_upload).click()
        self.find(self.__ele_reload_contact).click()
        from WebWeChatPO.page.contact_page import ContactPage
        return ContactPage(self.driver)
