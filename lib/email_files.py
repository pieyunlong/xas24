#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/26 11:24
# Author    : humengzhe
# @File     : email_files.py
# @Software : PyCharm
# smtplib 用于邮件的发信动作
# import logging
import smtplib
from lib.login import *
from email.mime.multipart import MIMEMultipart
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 构建邮件头
from email.header import Header
import config.config
from config.config import *
def send_email(report_file=report_file):
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = sender
    password = smtp_password
    # 收信方邮箱
    to_addr = receiver
    # 发信服务器
    smtp_server = 'smtp.qq.com'

    with open(report_file, encoding="utf-8") as f:
        email_body = f.read()
    msg = MIMEMultipart()
    msg.attach(MIMEText(email_body, "html", "utf-8"))
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    # msg = MIMEText('使用python发送邮件测试', 'plain', 'utf-8')
    # 邮件头信息
    msg['From'] = Header(sender)  # 发送者
    msg['To'] = Header(receiver)  # 接收者
    subject = config.config.subject
    msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题
    att1 = MIMEText(
        open(report_file, "rb").read(), "base64", "utf-8"
    )
    att1["Content-Type"] = "application/octet-stream"
    att1["Content-Disposition"] = "attachment;filename='report.html'"
    msg.attach(att1)
    try:
        smtpobj = smtplib.SMTP_SSL(smtp_server)
        # 建立连接--qq邮箱服务和端口号（可百度查询）
        smtpobj.connect(smtp_server, 465)
        # 登录--发送者账号和口令
        smtpobj.login(from_addr, password)
        # 发送邮件
        smtpobj.sendmail(from_addr, to_addr, msg.as_string())
        logging.info("发送邮件成功")
        print("邮件发送成功")
    except Exception as e:
        logging.debug("无法发送邮件")
        print("无法发送邮件")
    finally:
        # 关闭服务器
        smtpobj.quit()
if __name__ == '__main__':
    send_email("../report/report.html")