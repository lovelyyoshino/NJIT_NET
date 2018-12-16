#!/usr/bin/env python

#_*_conding:utf-8_*_
import requests
import urllib
import re
import subprocess
import time
import socket
import json
import os


USR    = ""
PWD    = ""
ips="119.75.217.109"

def load():
    global USR,PWD
    if os.path.exists('data.json'):
        try:
            with open('data.json','r') as f:
                data = json.load(f)
                USR=data.split(":",1)[0]
                PWD=data.split(":",1)[1]
        except:
            print("删除重新登录")
    else:
        USR    = input("账户：")
        PWD    = input("密码：")
        data=USR +":"+PWD
        with open('data.json', 'w') as fw:
            json.dump(data,fw)
def get_ip():
    myname = socket.getfqdn(socket.gethostname())
    s = socket.gethostbyname(myname)
    return s

def ping_ips(ips):
    for ip in ips.split(";"):
        ret = subprocess.Popen("ping -n 1 -w 1 %s " % ip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret.communicate()

        if ret.returncode == 0:
            print ("ping %s...successful!" % ip)
            return True
        else:
            print ("ping %s...failed!" % ip)

    return False



header_post = {
    'Origin': 'http://10.0.1.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)',
    'Referer': 'http://10.0.1.1/a70.htm',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'deflate',
}

if __name__ == "__main__":
    while 1:
        load()
        if(ping_ips(ips)==False):
            user_ip = get_ip()
            postData ={
                    'DDDDD'         : ',0,%s' % USR,
                    'upass'         : '%s' % PWD,
                    'R1'            : '0',
                    'R2'            : '0',
                    'R3'            : '0',
                    'R6'            : '0',
                    'para'          : '00',
                    '0MKKey'        : '123456',
                    'buttonClicked' : '',
                    'redirect_url'  : '',
                    'err_flag'      : '',
                    'username'      : '',
                    'password'      : '',
                    'user'          : '',
                    'cmd'           : '',
                    'Login'         : ''
                }
            #print(postData)
            url = "http://10.0.1.1:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.0.1.1&iTermType=1&wlanuserip=%s&wlanacip=null&wlanacname=njit_off&mac=00-00-00-00-00-00&ip=%s&enAdvert=0&queryACIP=0&loginMethod=1"%(user_ip,user_ip)
            #print(url)
            request = requests.post(url=url, data=postData, headers=header_post)
            #s=request.text.encode('utf-8').decode('unicode-escape')
            #print(s)
            print("登录检测中")
            time.sleep(1)
            if (ping_ips(ips) == True):
                print("登录成功")
        else:
            time.sleep(10*60)

