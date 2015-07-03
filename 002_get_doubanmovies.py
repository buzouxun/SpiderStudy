# -*- coding: utf-8 -*-

__author__ = 'jzhu'

import re
import urllib.request
from bs4 import BeautifulSoup


raw_url = 'http://movie.douban.com/chart'

# with urllib.request.urlopen(raw_url) as f:
#     # html = f.read(300).decode('utf-8')
#     html = f.read(300)
#
# print("html = \n", html.decode('utf-8'))

html = urllib.request.urlopen(raw_url).read()

'''
# html = urlopen(raw_url).read()

reg_name = r'<img src=".*" alt="(.*?)" class=""/>'
reg_introduction = r'<p class="pl">(.*)</p>'
reg_score= r'<span class="rating_nums">(.*?)</span>'
reg_evalute = r'<span class="pl">\((.*)\)</span>'

print('豆瓣新片排行榜')
print('-' * 80)

class DBM(object):
    def __init__(self, reg, html):
        self.reg, self.html = reg, html
    def __iter__(self):
        return self  #instance self is iteration object, so return self

    def get(self):
        m_list = re.findall(self.reg, self.html)
        u_list =[]
        for abc in m_list:
            u_abc = abc.decode('utf-8')
            u_list.append(u_abc)
        return u_list

name = DBM(reg_name, html)
a = name.get

intro = DBM(reg_introduction, html)
b = intro.get

score = DBM(reg_score, html)
c = score.get

evaluate = DBM(reg_evalute, html)
d = evaluate.get


def index(num):
    print(a()[num], ' ',  b()[num], ' ', 'Score:%s'%(c()[num]),' ', d()[num])
    print('')

nn = len(a())
for x in range(nn):
    index(x)
'''

import codecs

file = codecs.open('002_get_doubanmovies.txt', 'w', 'utf-8-sig')

# use bs4
soup = BeautifulSoup(html)

#本周口碑榜
week = soup.find('div', id='ranking').find('ul', id='listCont2')
file.write('-' * 80 + '\n')
file.write("本周口碑榜: \n")
file.write(soup.find('div', id='ranking').find('ul', id='listCont2').find('li').get_text())
for link in week.find_all('a'):
    text = link.get_text()
    text = text.strip()
    file.write('\t')
    file.write(text)
    file.write('\n')

#北美票房榜影名
week_name = soup.find('div', id='ranking').find('ul', id='listCont1')
america = []
for link in week_name.find_all('a'):
    america.append(link.get_text().strip())

#票房榜的钱
money = soup.find('div', id='ranking').find('ul', id='listCont1')
dollar = []
for m in money.find_all('span'):
    dollar.append(m.get_text().strip())
m_date = dollar.pop(0)

def split(num2):
    file.write("\t")
    file.write(america[num2])
    file.write(", ")
    file.write(dollar[num2])
    file.write("\n")


file.write("\n" + '-' * 80 + "\n")
file.write('北美票房榜:\n\n')
file.write(m_date)
file.write('\n')

lens = len(america)
for num2 in range(lens):
    split(num2)

file.close()











