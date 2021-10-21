# -*- coding:utf-8 -*-
# @time :2021-10-21  10:35
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_calc_fixrure.py

"""
验证获取数据用例
def test_add_datas(get_datas_calc_add):
    print(get_datas_calc_add)

def test_sub_datas(get_datas_calc_sub):
    print(get_datas_calc_sub)

def test_mul_datas(get_datas_calc_mul):
    print(get_datas_calc_mul)

def test_div_datas(get_datas_calc_div):
    print(get_datas_calc_div)
"""


class TestCalc:

    def test_adds(self, initcalc_class, get_datas_calc_add):
        assert get_datas_calc_add[2] == initcalc_class.add(get_datas_calc_add[0], get_datas_calc_add[1])
        print(
            f"{get_datas_calc_add[0]}+{get_datas_calc_add[1]}={initcalc_class.add(get_datas_calc_add[0], get_datas_calc_add[1])}")

    def test_sub(self, initcalc_class, get_datas_calc_sub):
        assert get_datas_calc_sub[2] == initcalc_class.sub(get_datas_calc_sub[0], get_datas_calc_sub[1])
        print(
            f"{get_datas_calc_sub[0]}+{get_datas_calc_sub[1]}={initcalc_class.sub(get_datas_calc_sub[0], get_datas_calc_sub[1])}")

    def test_mul(self, initcalc_class, get_datas_calc_mul):
        assert get_datas_calc_mul[2] == initcalc_class.mul(get_datas_calc_mul[0], get_datas_calc_mul[1])
        print(
            f"{get_datas_calc_mul[0]}+{get_datas_calc_mul[1]}={initcalc_class.sub(get_datas_calc_mul[0], get_datas_calc_mul[1])}")

    def test_div(self, initcalc_class, get_datas_calc_div):
        if get_datas_calc_div[1] == 0:
            print("除数不可为零")
            raise ZeroDivisionError
        else:
            assert get_datas_calc_div[2] == initcalc_class.div(get_datas_calc_div[0], get_datas_calc_div[1])
        print(
            f"{get_datas_calc_div[0]}+{get_datas_calc_div[1]}={initcalc_class.div(get_datas_calc_div[0], get_datas_calc_div[1])}")


'''
ids:
  add:
    - - "整数加法"
    - - "小数加法"
    - - "大整数加法"
    - - "含零加法"
  sub:
    - - "整数减法"
    - - "小数减法"
    - - "大整数减法"
    - - "含零减法"
  mul:
    - - "整数乘法"
    - - "小数乘法"
    - - "大整数乘法"
    - - "含零乘法"
  div:
    - - "整数除法"
    - - "小数可整除除法"
    - - "大整数除法"
    - - "含零除法"
'''

"""
ids:
  add:
    - - integer addition
    - - decimal addition
    - - large integer addition
    - - addition with zero
  sub:
    - - integer subtraction
    - - decimal subtraction
    - - large integer subtraction
    - - subtraction with zero
  mul:
    - - integer multiplication
    - - decimal multiplication
    - - large integer multiplication
    - - multiplication with zero
  div:
    - - integer division
    - - decimal divisible division
    - - large integer division
    - - division with zero
"""
