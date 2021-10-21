# -*- coding:utf-8 -*-
# @time :2021-10-21  10:06
# @Author :Tyz
# @Email :910771232@qq.com
# @file :fixture_param.py
import pytest


@pytest.fixture(params = [["Jerry", 123], ["Ken", 456], ["Lily", 789]], ids = ["user1", "user2", "user3"])
def login(request):
    # 根据fixture本身的定义，request 和 request.param  都是固定的写法
    print("login")
    return request.param


def test_longin(login):
    print(login)
