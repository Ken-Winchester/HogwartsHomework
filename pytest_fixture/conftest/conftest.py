# -*- coding:utf-8 -*-
# @time :2021-10-21  9:42
# @Author :Tyz
# @Email :910771232@qq.com
# @file :conftest.py


import pytest


@pytest.fixture()
def connectDb():
    print("连接数据库")
    return "搜索结果"


@pytest.fixture()
def login(connectDb):
    print("login")
    username = "hogwarts"
    password = "ceshiren"
    return username, password
