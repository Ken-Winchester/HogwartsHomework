# -*- coding:utf-8 -*-
# @time :2021-10-21  19:58
# @Author :Tyz
# @Email :910771232@qq.com
# @file :conftest.py
from typing import List

import pytest


def pytest_collection_modifyitems(session, config, items: List):
    print("这是收集所有测试用例的方法")
    print(items)
    items.reverse()
    for item in items:
        if "foo" in item.name:
            item.add_marker(pytest.mark.foo)
        elif "last" in item.name:
            item.add_marker(pytest.mark.last)
