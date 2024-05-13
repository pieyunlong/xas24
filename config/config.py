#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/28 10:22
# Author    : humengzhe
# @File     : config.py
# @Software : PyCharm
import logging,os,time
from optparse import OptionParser

now = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))

# 获取文件位置（os.path.dirname是文件绝对路径的上一级）
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 获取数据目录暂时在项目路径下
data_path=prj_path
# 用例目录录暂时在项目路径下
test_path = os.path.join(prj_path,"data","test_user_data0.xlsx")
# 生成日志文件
log_file = os.path.join(prj_path,"log", "log_{}.txt".format(today))
# 生成测试报告
report_file = os.path.join(prj_path,"report", "report_{}.html".format(now))
# 测试文件
test_case_path = os.path.join(prj_path,"test","case")
# 具体测试文件
testlist_path = os.path.join(prj_path,"test","textlist.txt")
# 错误的测试文件
test_last_fails =  os.path.join(prj_path,"last_fails.pickie")
# log历史文件
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file,
    # encoding='utf-8',
    filemode='a'
)
# 数据库的数据
db_host = "localhost"
db_port = 3306
db_user = "root"
db_passwd = "root"
db = "xzs"
# 邮箱数据
smtp_server = "smtp.qq.com"
smtp_user = "3132541928@qq.com"
smtp_password = "srngnykxyombddfd"
sender = smtp_user
receiver = "3132541928@qq.com"
subject = "接口测试报告"
send_email_enable = False
# 命令行数据
parser = OptionParser()
parser.add_option("--collect_only",dest ="collect_only",action = "store_true",help = "收集测试用例但不执行")
parser.add_option("--rerun_fails",dest ="rerun_fails",action = "store_true",help = "重跑失败用例")
parser.add_option("--get",dest ="get",action = "store",help = "指定测试用例")
(options,args) = parser.parse_args()