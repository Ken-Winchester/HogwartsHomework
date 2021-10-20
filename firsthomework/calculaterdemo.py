# -*- coding:utf-8 -*-
# @time :2021-10-20  9:44
# @Author :Tyz
# @Email :910771232@qq.com
# @file :calculaterdemo.py


class Calculater:

    def add(self, a, b):
        return a + b

    def sub(self, c, d):
        return c - d

    def mul(self, e, f):
        return e * f

    def div(self, g, h):
        if h == 0:
            print("除数不可为零")
            pass
        else:
            return g / h
