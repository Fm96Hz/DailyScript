import smtplib
import string,sys
from email.mime.text import MIMEText

HOST = "smtp.163.com"
#SUBJECT = "The test email"
SUBJECT = "数据报表"
TO = "jack456645@qq.com"
FROM = "18339699712@163.com"
'''#简单内容
context = "This is Python email test"
BODY = "\r\n".join((
    "FROM: %s" % FROM ,
    "TO: %s" % TO,
    "SUBJECT: %s" % SUBJECT,
    "",
    context
))
print(BODY)
server = smtplib.SMTP_SSL()
server.connect(HOST,"465")
try:
    server.login("18339699712@163.com","IKNBXLQRYCPDPUEH")
    server.sendmail(FROM,[TO],BODY)
    server.quit
except Exception as e:
    print("ERROR: %s" % e)
    server.quit'''
#基于HTML格式定制数据报表邮件  需要用到 MIMEText 类
msg = MIMEText("""
    <table width="800" border="0" cellspacing="0" cellpadding="4">
      <tr>
        <td bgcolor="#CECFAD" height="20" style="font-size:14px">*官网数据  <a href="monitor.domain.com">更多>></a></td>
      </tr>
      <tr>
        <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
        1）日访问量:<font color=red>152433</font>  访问次数:23651 页面浏览量:45123 点击数:545122  数据流量:504Mb<br>
        2）状态码信息<br>
        &nbsp;&nbsp;500:105  404:3264  503:214<br>
        3）访客浏览器信息<br>
        &nbsp;&nbsp;IE:50%  firefox:10% chrome:30% other:10%<br>
        4）页面信息<br>
        &nbsp;&nbsp;/index.php 42153<br>
        &nbsp;&nbsp;/view.php 21451<br>
        &nbsp;&nbsp;/login.php 5112<br>
	</td>
      </tr>
    </table>""","html","utf-8")
msg["Subject"] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
try:
    server = smtplib.SMTP_SSL()
    server.connect(HOST,"465")
    server.login("18339699712@163.com","IKNBXLQRYCPDPUEH")
    server.sendmail(FROM,TO,msg.as_string())
    server.quit()
except Exception as e:
    print("ERROR:"+str(e))
