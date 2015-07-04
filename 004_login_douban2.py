# -*- coding:utf-8 -*-

__author__ = 'jzhu'


''' 使用requests登录豆瓣，获取豆邮列表 '''
import requests
import re
from bs4 import BeautifulSoup
import random
import urllib
import datetime
import codecs

file = codecs.open('004_login_douban2.txt', 'w', 'utf-8-sig')

login_url = "http://www.douban.com/accounts/login"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',}

my_post = {'redir':'http://www.douban.com/doumail',
    'form_email':'zjyhou@126.com',
    'form_password':'password',
    'login':'登录',
    }
r = requests.post(login_url, data = my_post, headers = headers)
html = r.text

'''  download captcha  '''
reg = r'<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>'
imglist = re.findall(reg, html)
if imglist.__len__() > 0:
    print("imglist.length = ", imglist.__len__())
    urllib.request.urlretrieve(imglist[0], '004_login_douban2_%s.jpg' % str(datetime.datetime.now().strftime("%H-%M-%S")))
    captcha = input('captcha is: ')
    regid = r'<input type="hidden" name="captcha-id" value="(.*?)"/>'
    ids = re.findall(regid, html)

''' repost  '''
if imglist.__len__() > 0:
    my_post["captcha-solution"] = captcha
    my_post["captcha-id"] = ids[0]
q = requests.post(login_url, data = my_post, headers = headers)
print(q.url)

''' use bs4 filter douban.com's doumail following'''
if q.url == "http://www.douban.com/doumail/":
    print(" login successfully!")
    soup = BeautifulSoup(q.text)
    tag = soup.find_all('span', attrs={'class':'from'})
    tag2 =  soup.find_all('a', attrs={'class':'url'})

    print("tag.size =  ", tag.__len__())
    print("tag2.size = ", tag2.__len__())

    a = []
    for x in tag:
        a.append(x.get_text())
    b = []
    for y in tag2:
        b.append(y.get_text())

    def split(num):
        file.write("\t" + a[num] + '  ' +  b[num] + "\n")

    file.write("\n" + '-'*30 + '豆瓣豆邮' + '-'*30 + "\n")
    for x in range(len(a)):
        split(x)
    file.write('-'*80)

file.close()