# -*- coding:utf-8 -*-
# @time :2021-10-21  10:33
# @Author :Tyz
# @Email :910771232@qq.com
# @file :conftest.py

import pytest
import yaml
from calculaterx import Calculater1
from typing import List


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


'''    
def setup_class(self):
    print("开始计算")

def teardown_class(self):
    print("计算结束")
'''


@pytest.fixture(scope = "class")
def initcalc_class():
    # setup
    print("开始计算")
    calc = Calculater1()
    yield calc
    # teardown
    print("计算结束")


# @pytest.fixture(scope = "module")
def get_datas():
    with open("./datas.yaml", encoding = "utf-8") as f:
        datas = yaml.safe_load(f)
    return datas


'''
验证文件读写用例
def test_getdatas(get_datas):
    print(get_datas)
'''


@pytest.fixture(params = get_datas()["int_datas"]["add_data"], ids = get_datas()["ids"]["add_title"])
def get_datas_calc_add(request):
    return request.param


@pytest.fixture(params = get_datas()["int_datas"]["sub_data"], ids = get_datas()["ids"]["sub_title"])
def get_datas_calc_sub(request):
    return request.param


@pytest.fixture(params = get_datas()["int_datas"]["mul_data"], ids = get_datas()["ids"]["mul_title"])
def get_datas_calc_mul(request):
    return request.param


@pytest.fixture(params = get_datas()["int_datas"]["div_data"], ids = get_datas()["ids"]["div_title"])
def get_datas_calc_div(request):
    return request.param


''''''
