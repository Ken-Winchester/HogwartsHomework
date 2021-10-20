# -*- coding:utf-8 -*-
# @time :2021-10-20  7:59
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_param.py
import pytest
from calculatordemo.Calculator import Calculator


@pytest.mark.parametrize("key,result", [["appuim", 200], ["selenium", 300], ["request", 400]])
def test_interface(key, result):
    url = f"https://ceshiren.com/key={key}"
    print(url, result)


class TestAdd:
    def setup(self):
        print("setup")
        self.cal = Calculator()

    def teardown(self):
        print("teardown")

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [0.1, 0.1, 0.2], [1000, 1000, 2000], [0, 1000, 1000]],
                             ids = ["int1", "float", "bignum", "zeronum"])
    def test_adds(self, a, b, expect):
        assert expect == self.cal.add(a, b)


@pytest.mark.parametrize("c", ["x", "y", "z"])
@pytest.mark.parametrize("b", [1, 2, 3])
@pytest.mark.parametrize("a", ["int", "float", "string"])
def test_cartesian_product(a, b, c):
    print(a, b, c)
