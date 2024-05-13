#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/23 15:12
# Author    : humengzhe
# @File     : 224660423裴云龙4.23.py
# @Software : PyCharm
import xlrd
class xlrd_deom():
    def xlrd_in(self,name,name_sheet):
        # 打开文件
        wd = xlrd.open_workbook(name)
        # 打开文件后打开表
        sheet = wd.sheet_by_name(name_sheet)
        # 打开第几个表
        # sheet = wd.sheet_by_index(1)
        # 固定key值
        keys = sheet.row_values(0)
        # 获取行
        # print(sheet.nrows)
        # 获取列
        # print(sheet.ncols)
        # 创建空列表
        list=[]
        # 循环表中数据将数据放到列表中
        for i in range(1,sheet.nrows):
            list.append(dict(zip(keys,sheet.row_values(i))))
        return list
    def xlrd_get(self,list,test_name):
        # 循环列表
        for i in list:
            # 判断列表中是否有查找的值没有返回空值    dict[]等同dict.get("name")
            if test_name == i["test_name"]:
                return i
if __name__ == '__main__':
    a = xlrd_deom()
    l = a.xlrd_in("test_user_data0.xlsx","test_user_login")
    r = a.xlrd_get(l, "test_ok")
