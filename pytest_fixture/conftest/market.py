# -*- coding:utf-8 -*-
# @time :2021-10-21  9:43
# @Author :Tyz
# @Email :910771232@qq.com
# @file :market.py
import pytest


def test_search(connectDb):
    print(connectDb)
    print("搜索")


def test_add_cart(login):
    print("添加到购物车")


def test_order(login):
    username, password = login
    print(username, password)
    print("订单")
