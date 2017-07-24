from email.mime.multipart import MIMEMultipart

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time
import unittest
import os
import  sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\WebAuto\\test_case\\")

from readconfig import readconfig
from comm.sendEmail import send_mail,new_report
localReadConfig = readconfig()

# #==========定义发送邮件=========
# def send_mail(new_file):
#     print(new_file)
#     f = open(new_file,"rb")
#     mail_body = f.read()
#     f.close()
#
#     msg =MIMEText(mail_body,"html","utf-8")
#     # msg["Content-Type"]='application/octet-stream'
#     # msg["Content-Disposition"]='attachment,filename="uni-ubi.html"'
#     # msgRoot=MIMEMultipart('related')
#     # subject="登录界面自动化测试报告"
#     # msg["Subject"]=subject
#     msg["Subject"]=Header("登录界面自动化测试报告","utf-8")
#     # msgRoot.attach(msg)
#     msg['From'] = localReadConfig.get_email("sender")
#     msg['To'] = localReadConfig.get_email("receiver")
#
#     smtp=smtplib.SMTP()
#     smtp.connect("smtp.126.com")
#     smtp.starttls()
#     print("126邮箱登入前")
#     smtp.login("qq741562314@126.com","a115211")
#     print("126邮箱登入成功")
#     smtp.sendmail("qq741562314@126.com","741562314@qq.com",msg.as_string())
#     print("126发送邮件成功")
#     smtp.quit()
#     print("mail has send out")
#
#
#
# #=====================查找测试报告目录，找到最新生产的测试报告文件====================
# def new_report(testreport):
#     lists=os.listdir(testreport)
#     lists.sort(key=lambda fn:os.path.getatime(testreport + "\\" +fn))
#     file_new=os.path.join(testreport,lists[-1])
#     print(testreport)
#     print(file_new)
#     return file_new


def runAll():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    file_name = "../report/" + now + "result.html"
    fp = open(file_name, "wb")
    runner = HTMLTestRunner(stream=fp, title="UniUbi登入测试报告", description="环境：W8，浏览器：firefox")
    discover=unittest.defaultTestLoader.discover("./",pattern="logintest.py")

    runner.run(discover)
    # 单个测试用例运行
    suite = unittest.TestSuite()
    # suite.addTest(add_sta.addTest("test_add1"))
    # runner.run(suite)
    fp.close()
    file_path = new_report("../report/")
    send_mail(file_path)

if __name__=="__main__":

    runAll()