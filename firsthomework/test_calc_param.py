# -*- coding:utf-8 -*-
# @time :2021-10-20  9:45
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_calc_param.py
import pytest
import yaml
from calculaterdemo import Calculater


def get_datas():
    with open("./datas.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


def test_getdatas():
    with open("./datas.yaml") as f:
        datas = yaml.safe_load(f)
    print(datas)


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

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./calc_add.yaml")),
                             ids = ["整数加法", "小数加法", "大整数加法", "含零加法"])
    def test_adds(self, a, b, expect):
        assert expect == self.calc.add(a, b)
        print(f"{a}+{b}={self.calc.sub(a, b)}")

    @pytest.mark.parametrize("c,d,expect", yaml.safe_load(open("./calc_sub.yaml")),
                             ids = ["整数减法", "小数减法", "大整数减法", "含零减法"])
    def test_sub(self, c, d, expect):
        assert expect == self.calc.sub(c, d)
        print(f"{c}+{d}={self.calc.sub(c, d)}")

    @pytest.mark.parametrize("e,f,expect", yaml.safe_load(open("./calc_mul.yaml")),
                             ids = ["整数乘法", "小数乘法", "大整数乘法", "含零乘法"])
    def test_mul(self, e, f, expect):
        assert expect == self.calc.mul(e, f)
        print(f"{e}+{f}={self.calc.mul(e, f)}")

    @pytest.mark.parametrize("g,h,expect", yaml.safe_load(open("./calc_div.yaml")),
                             ids = ["整数除法", "小数可整除除法", "大整数除法", "含零除法"])
    def test_div(self, g, h, expect):
        if h == 0:
            print("除数不可为零")
            raise ZeroDivisionError
        else:
            assert expect == self.calc.div(g, h)
        print(f"{g}+{h}={self.calc.div(g, h)}")

    @pytest.mark.parametrize("a,b,expect", get_datas()["int_datas"], ids = get_datas()["ids"])
    def test_add_int(self, a, b, expect):
        assert expect == self.calc.add(a, b)
        print(f"{a}+{b}={self.calc.add(a, b)}")
