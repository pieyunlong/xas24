#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/19 9:03
# Author    : humengzhe
# @File     : db.py
# @Software : PyCharm
import pymysql
from lib.login import *
from config.config import *
# 创建链接
def con():
    con = pymysql.connect(host=db_host,user=db_user,
                        password=db_passwd,port=db_port,
                        database=db,charset="utf8")
    return con
#创建sql查询
def cursor(sql):
    # 创建连接
    conm = con()
    # 创建游标
    cur = conm.cursor()
    # 将sql语句写入日志文件
    logging.info(sql)
    # 执行sql语句
    cur.execute(sql)
    a = cur.fetchall()
    return a
def change_db(sql):
    conm = con()
    cur = conm.cursor()
    # 将sql语句写入日志文件
    logging.info(sql)
    try:
        # 执行sql语句
        cur.execute(sql)
        # 提交操作
        conm.commit()
    except Exception as a:
        # 将错误信息语句写入日志文件
        logging.info(a)
        # 回滚
        conm.rollback()
    finally:
        # 关闭连接
        cur.close()
        # 关闭游标
        conm.close()
#     查询
def check_user(name):
    sql = "SELECT * FROM t_user WHERE user_name = '{}'".format(name)
    # 执行sql语句
    a = cursor(sql)
    return True if a else False
#  添加
def add_user(name,password):
    sql = "insert into t_user(user_name,password) values ('{}','{}')".format(name,password)
    # 执行添加sql语句
    print(sql)
    a = change_db(sql)
    return True if a else False
# 删除
def del_user(name):
    # 执行删除sql语句
    sql = "delete from t_user where user_name = '{}'".format(name)
    a = change_db(sql)
    return True if a else False