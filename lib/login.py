#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/26 8:48
# Author    : humengzhe
# @File     : login.py
# @Software : PyCharm
import logging

# class log():
#     def __init__(self):
#         logging.basicConfig(level=logging.DEBUG,        #控制台打印的日志级别
#                          filename='log.txt',
#                          filemode='a',      #  追加模式，默认如果不写的话，就是追加模式
#                          format='%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s')
#                          # 时间。位置。等级。内容。
#
#     def log_w(self,msg):
#         logging.warning(msg)
# if __name__ == '__main__':
#     a = log()
#     a.log_w("接口测试")
import logging
from config.config import *
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file,
    # encoding='utf-8',
    filemode='a'
)
if __name__ == '__main__':
    logging.info("接口测试")