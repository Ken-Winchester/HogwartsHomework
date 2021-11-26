# -*- coding:utf-8 -*-
# @time :2021-11-26  13:29
# @Author :Tyz
# @Email :910771232@qq.com
# @file :conftest.py
from typing import List


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
