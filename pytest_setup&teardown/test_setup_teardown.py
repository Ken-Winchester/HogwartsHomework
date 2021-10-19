# -*- coding:utf-8 -*-
# @time :2021-10-19  23:14
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_setup_teardown.py

# 类之外的setup
import pytest


def setup_function():
    print("setup_function")


# 类之外的teardown
def teardown_function():
    print("teardown_function")


def test_case1():
    print("case1")


class TestCase2:

    def setup_class(self):
        print("class_setup")

    def teardown_class(self):
        print("class_teardown")

    def test_case2(self):
        print("case2")

    def test_case3(self):
        print("case3")

    def test_case4(self):
        print("case4")


if __name__ == '__main__':
    pytest.main(["test_setup_teardown.py", "-vs"])
