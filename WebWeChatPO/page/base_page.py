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
        if self.driver == None:
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
        else:
            self.driver = base_driver

    # login = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"
    # wechat_cookies = self.driver.get_cookies()
