# -*- coding: utf-8 -*-
__author__ = 'jzhu'

#使用urllib, urllib2模拟登录豆瓣，获取豆邮列表邮

import urllib
import urllib.request
from http.cookiejar import CookieJar
import random
import re
from bs4 import BeautifulSoup
import codecs

# file = codecs.open('003_login_douban1.txt', 'w', 'utf-8-sig')

class DB(object):
    def __init__(self, email, passwd):
        self.url = "http://www.douban.com/accounts/login"
        self.post = {
            'form_email':email,
            'form_password':passwd,
            'source':'index_nav'
            }
        cookie = CookieJar()
        # self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        # self.response = self.opener.open(self.url, urllib.request.urlencode(self.post))
        # self.response = self.opener.open(self.url, urllib.parse.urlencode(self.post))
        self.response = self.opener.open(self.url)

    def login(self):
        if self.response.geturl() == self.url:
            print('logining...')
            html = self.response.read()
            reg = r'<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>'
            imglist = re.findall(reg, html.decode('utf-8'))
            urllib.request.urlretrieve(imglist[0], '%d.jpg' % random.randint(1,100))
            captcha = input('captcha is: ')
            regid = r'<input type="hidden" name="captcha-id" value="(.*?)"/>'
            ids = re.findall(regid, html)
            self.post["captcha-solution"] = captcha
            self.post["captcha-id"] = ids[0]
            self.post["user_login"] = "登录"
            self.post["redir"] = 'http://www.douban.com/doumail/'
            if self.response.geturl() == "http://www.douban.com/doumail/":
                print('login success !')
                # soup = BeautifulSoup(self.response.read())
                # tag = soup.find_all('span', attrs={'class':'from'})
                # tag2 =  soup.find_all('a', attrs={'class':'url'})
                # a = []
                # for x in tag:
                #     a.append(x.get_text())
                # b = []
                # for y in tag2:
                #     b.append(y.get_text())
                #
                # def split(num):
                #     print(a[num] + '  ' +  b[num])
                #     print()
                #
                # print('-'*30, '豆瓣豆邮', '-'*30)
                # for x in range(len(a)):
                #     split(x)
                # print('-'*80)

# email = input('Your email: ')
# passwd = input('Your passwd: ')
email = "zjyhou@126.com"
passwd = "password"
my = DB(email, passwd)
my.login()

# file.close()