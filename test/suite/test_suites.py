#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/7 15:23
# Author    : humengzhe
# @File     : test_suites.py
# @Software : PyCharm
import unittest,sys
sys.path.append("../..")
from test.case.user.BaseCase1 import test_user_login
from test.case.user.BaseCase2 import test_user_reg
smoke_suite = unittest.TestSuite()
smoke_suite.addTests([test_user_login("test01"),test_user_reg("test_mysql_ok1")])
def get_suite(suite_name):
    smoke_suite = unittest.TestSuite()
    smoke_suite.addTests([test_user_login("test01"),test_user_reg("test_mysql_ok1")])
    return suite_name
# unittest.TextTestRunner(verbosity=2).run(smoke_suite)