#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'send smtp3.hp.com mail'
___author__ = 'wr'
from email.mime.text import MIMEText
import smtplib
class SendMail(object):
    def __init__(self,to_addr,message):
        self.msg = MIMEText(message, 'plain', 'utf-8')
        # 输入Email地址和口令:
        self.from_addr = 'PythonInsert@hp.com'
        self.password = '***'
        # 输入收件人地址:
        self.to_addr = to_addr
        # 输入SMTP服务器地址:
        self.smtp_server = 'smtp3.hp.com'
        server = smtplib.SMTP(self.smtp_server, 25) # SMTP协议默认端口是25
        server.set_debuglevel(1)
        # server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.quit()
if __name__=='__main__':
    s = SendMail('*****@hp.com','pthon test send ')
    print('ok')























