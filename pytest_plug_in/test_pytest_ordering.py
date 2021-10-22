# -*- coding:utf-8 -*-
# @time :2021-10-21  19:43
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_pytest_ordering.py
import allure
import pytest


@allure.story("ssd")
@pytest.mark.twentieth
# @pytest.mark.run(order = 20)  作用同上一行
def test_foo():
    assert True


@allure.story("aad")
@pytest.mark.last
# @pytest.mark.run(order = -1)  作用同上一行
def test_last():
    assert True


@allure.story("sad")
@pytest.mark.first
# @pytest.mark.run(order = 0)  作用同上一行
def test_bar():
    assert True
