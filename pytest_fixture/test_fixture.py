# -*- coding:utf-8 -*-
# @time :2021-10-21  8:41
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_fixture.py
import pytest


# Attention the effect of fixture with scope
# scope = "function(default),class,module,package,project,session"
# @pytest.fixture(autouse = True)
# def test_setup1():
#     print("测试autouse")


@pytest.fixture()
def connectDb():
    print("连接数据库")
    return "搜索结果"


'''
# fixture&yield
@pytest.fixture()
def connectDb1():
    # 相当于setup
    print("连接数据库")
    # return "database datas"
    yield "搜索结果" # 返回后面的结果
    # 相当于 teardown
    print("断开连接数据")
'''


@pytest.fixture()
def login(connectDb):
    print("login")
    username = "hogwarts"
    password = "ceshiren"
    return username, password


# @pytest.mark.usefixtures("connectDb")
def test_search(connectDb):
    print(connectDb)
    print("搜索")


@pytest.mark.usefixtures("connectDb")
def test_search1():
    print(connectDb)
    print("搜索")


# Attention!!! Fixtures are not meant to be called directly, like connectDB() down here.
# def test_search2():
#     print(connectDb())
#     print("搜索")


@pytest.mark.usefixtures("login")
def test_add_cart():
    print("添加到购物车")


def test_order(login):
    username, password = login
    print(username, password)
    print("订单")
