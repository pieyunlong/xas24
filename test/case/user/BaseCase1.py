#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/6 10:51
# Author    : humengzhe
# @File     : BaseCase1.py
# @Software : PyCharm
from test.case.BaseCase import BaseCase
class test_user_login(BaseCase):
    def test01(self):
        case_data = self.get_case_data("test_ok")
        self.send_request(case_data)
    def test02(self):
        case_data = self.get_case_data("test_err1")
        self.send_request(case_data)
if __name__ == '__main__':
    test_user_login()
