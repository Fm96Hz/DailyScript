#探测WEB服务质量
import pycurl
import time,sys
import os

URL = "http://www.baidu.com"
c = pycurl.Curl()
c.setopt(pycurl.URL,URL)   #定义请求的URL常量
c.setopt(pycurl.CONNECTTIMEOUT,5)    #定义请求连接的等待时间
c.setopt(pycurl.TIMEOUT,5)   #定义请求超时时间
c.setopt(pycurl.NOPROGRESS,1)   #屏蔽下载进度条
c.setopt(pycurl.FORBID_REUSE,1)   #完成交互后强制断开连接
c.setopt(pycurl.MAXREDIRS,1)   #指定HTTP重定向的最大数为1
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)  #设置保存DNS信息时间为30s

indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
c.setopt(pycurl.WRITEHEADER,indexfile)
c.setopt(pycurl.WRITEDATA,indexfile)
try:
    c.perform()
except Exception as e:
    print("connecion error:"+str(e))
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOK_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)

STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME )
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

print("HTTP状态码: %s" % (HTTP_CODE))
print("DNS解析时间：%.2f ms" % (NAMELOOK_TIME*1000))
print("建立连接时间：%.2f ms" % (CONNECT_TIME*1000))
print("准备传输时间：%.2f ms" % (PRETRANSFER_TIME*1000))
print("传输开始时间：%.2f ms" % (STARTTRANSFER_TIME*1000))
print("传输结束总时间：%.2f ms" % (TOTAL_TIME*1000))
print("下载数据包大小: %d bytes/s" % (SIZE_DOWNLOAD))
print("HTTP头部大小 %d byte" % (HEADER_SIZE))
print("平均下载速度：%d bytes/s" % (SPEED_DOWNLOAD))
indexfile.close()
c.close()

