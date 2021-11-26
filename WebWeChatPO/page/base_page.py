# -*- coding:utf-8 -*-
# @time :2021-11-26  12:46
# @Author :Tyz
# @Email :910771232@qq.com
# @file :base_page.py
import time
import yaml
from selenium import webdriver


class BasePage:
    """
    把页面重复的步骤抽离出来，封装:
    driver实例化
    """

    def __init__(self, base_driver = None):
        if base_driver:
            self.driver = base_driver
        else:
            # 实例化driver
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            # 访问扫码页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            time.sleep(3)
            with open("../wechat_cookies.yaml", encoding = "utf-8") as f:
                yaml_data = yaml.safe_load(f)
            print(yaml_data)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            time.sleep(5)

    def find(self, by, ele = None):
        """

        :param by:元素定位方式：CSS,XPATH,ID... 或 元素定位信息的元组（By.ID, “123”）
        :param ele:元素定位信息的值 “//*[text()=’元素‘]”
        :return:
        """

        # 两种传入定位元素方式，提高代码兼容性
        if ele is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)

    def quit(self):
        self.driver.quit()
