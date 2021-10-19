# -*- coding:utf-8 -*-
# @time :2021-10-19  22:42
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_cal.py

import pytest
from calculatordemo.Calculator import Calculator


class TestCal:

    def teardown(self):
        print("teardown")

    def setup(self):
        print("setup")
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(1, 1) == 2

    # def test_add1(self):
    #     assert 2.2 == self.calc.add(1.1, 1.1)

    def test_sub(self):
        assert 2 == self.calc.sub(3, 1)

    def test_mul(self):
        assert 2 == self.calc.mul(1, 2)

    def test_div(self):
        assert 2 == self.calc.div(4, 2)


if __name__ == '__main__':
    pytest.main(["test_cal.py::TestCal", "-vs", "--junitxml=./result.xml/"])
