# -*- coding:utf-8 -*-
# @time :2021-11-01  16:27
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_js.py
import time
from browserselect import Base
import pytest


class TestJS(Base):

    def test_js_datetimepicker(self):
        self.driver.get("https://www.12306.cn/index")
        date_js = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        print(date_js)
        time.sleep(2)
        self.driver.execute_script("a.value='2021-11-11'")
        print("打印")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        time.sleep(10)

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("seleniumJS测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[.='下一页 >']").click()
        time.sleep(3)
        # 单独执行可以return每一个命令的返回结果
        # for code in ["document.title", "return JSON.stringify(performance.timing)"]:
        #     print(self.driver.execute_script(code))

        # 合并执行只能返回第一个return的命令结果
        print(self.driver.execute_script("document.title;return JSON.stringify(performance.timing)"))
