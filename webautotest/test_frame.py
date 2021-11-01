# -*- coding:utf-8 -*-
# @time :2021-11-01  16:08
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_frame.py
from browserselect import Base
import time


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
