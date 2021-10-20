# -*- coding:utf-8 -*-
# @time :2021-10-20  9:45
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_calc_param.py
import pytest
import yaml
from firsthomework.calculaterdemo import Calculater


class TestCalc:

    def setup_class(self):
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    def setup(self):
        print("setup")
        self.calc = Calculater()

    def teardown(self):
        print("teardown")

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./calc_add.yaml")))
    def test_adds(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("c,d,expect", yaml.safe_load(open("./calc_sub.yaml")))
    def test_sub(self, c, d, expect):
        assert expect == self.calc.sub(c, d)

    @pytest.mark.parametrize("e,f,expect", yaml.safe_load(open("./calc_mul.yaml")))
    def test_mul(self, e, f, expect):
        assert expect == self.calc.mul(e, f)

    @pytest.mark.parametrize("g,h,expect", yaml.safe_load(open("./calc_div.yaml")))
    def test_div(self, g, h, expect):
        assert expect == self.calc.div(g, h)
