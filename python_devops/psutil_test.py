from _typeshed import ReadableBuffer
from dns.rdatatype import RdataType
from dns.tsig import get_context
import psutil
from subprocess import PIPE
import dns.resolver,os,http,httplib2
from IPy import IP
#采集系统信息：cpu、内存、磁盘、网络
#基于flask框架搭建运维系统后端基础
#psutil.cpu_count(logical=False)
#mem=psutil.virtual_memory()
'''p = psutil.Process(22441)
print(p.name())
print(p.exe())
print(p.status())
print(p.create_time())
print(p.uids())
print(p.gids(),p.cpu_times(),p.cpu_affinity(),p.memory_percent,p.memory_info(),p.io_counters(),p.connections())

p1=psutil.Popen(["/bin/python","-c","print('hello')"],stdout=PIPE)
print(p1.name(),p1.username(),p1.communicate(),p1.cpu_times())'''
#print(IP('192.138.1.0').make_net('255.255.255.0'))
appdomain = input("Please input an domain: ")
iplist=[]
def get_iplist(appdomain):
    try:
        A = dns.resolver.query(appdomain,'A')
    except Exception as e:
        print ("dns resolver errir:"+str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                iplist.append(j.address)
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontext=""
    httplib2.HTTPConnectionWithTimeout(5)
    conn=httplib2.HTTPConnection(checkurl)
    try:
        conn.request("GET","/","headers = {"Host": appdomain})
        r=conn.getresponse()
        getcontext=r.read(15)
    finally:
        if getcontext == "<!doctype html>":
            print ip+"[ok]"
        else:
            print ip+"[error]"

if __name__==__main__:
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print("dns resovler error.")

