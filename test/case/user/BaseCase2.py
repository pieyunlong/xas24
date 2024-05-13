#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/7 15:42
# Author    : humengzhe
# @File     : BaseCase2.py
# @Software : PyCharm
import json

from test.case.BaseCase import BaseCase
from lib.db import *

class test_user_reg(BaseCase):
    def test_mysql_ok1(self):
        case_data = self.get_case_data("test_ok")
        name = case_data["args"]
        name = json.loads(name)
        notname = name["userName"]
        if check_user(notname):
            del_user(notname)
        self.send_request(case_data)
        del_user(notname)
    def test_mysql_er1(self):
        case_data = self.get_case_data("test_err1")
        name = case_data["args"]
        name = json.loads(name)
        name = name["userName"]
        if  check_user(name):
            pass
        else:
            add_user(name,"123456")
        self.send_request(case_data)

if __name__ == '__main__':
    test_user_reg()