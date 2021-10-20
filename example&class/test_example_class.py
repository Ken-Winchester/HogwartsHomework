# -*- coding:utf-8 -*-
# @time :2021-10-20  8:53
# @Author :Tyz
# @Email :910771232@qq.com
# @file :test_example_class.py

class Person:

    def get_name(self):
        return "hogwarts"

    def get_age(self):
        print("31")

    def get_gender(self):
        # 这里的self.get_name()相当于下面的Person().get_name()
        print(self.get_name())
        print("male")

    @classmethod
    def get_money(cls):
        return 10000


def test_case123():
    Person().get_age()
    print(Person().get_name())
    Person().get_gender()
    print(Person.get_money())
