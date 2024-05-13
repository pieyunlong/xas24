#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/26 9:39
# Author    : humengzhe
# @File     : login_xzs_log.py
# @Software : PyCharm
import json

from lib.login import *

def login_xzs(text_name,url,args,expect_res,res_text):
    if isinstance(args,dict):
        args = json.dumps(args,ensure_ascii=False)
    logging.info("测试用例:{}".format(text_name))
    logging.info("url:{}".format(url))
    logging.info("请求参数:{}".format(args))
    logging.info("期望结果:{}".format(expect_res))
    logging.info("实际结果:{}".format(res_text))
if __name__ == '__main__':
    logging.info("接口测试")