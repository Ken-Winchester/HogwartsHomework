# -*- coding:utf-8 -*-
# @time :2021-10-21  17:00
# @Author :Tyz
# @Email :910771232@qq.com
# @file :assert_extend.py
from hamcrest import *


def add_hamcrest(a, b):
    print(assert_that((a + b), matcher = close_to(100, 120)))


add_hamcrest(10, 91)
