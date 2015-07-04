from urllib.request import urlopen, urlretrieve

__author__ = 'jzhu'

# ??????
# http://tieba.baidu.com/p/3864622302?fr=frs
# http://users.wpi.edu/~jzhu1/cs4241/assignment2/index.html

import re
import urllib

a = "http://quiet-wave-8700.herokuapp.com/home?show=Welcome!"
# a = input('input url: ')
if "http" not in a:
    a = "http://" + str(a);
print("a = \n", a)

s = urlopen(a)
# print("s = \n", s)

urlread = s.read()
print("urlread = \n", urlread)

def getimgs(urlread):
    res = []
    # reg = re.compile('src="[http/]')
    reg = re.compile(r'<img[\w\b\s\S]*src=[\w\b\s\S]*alt')
    l = re.findall(reg, urlread)
    print("l.size() = \n", l.__len__())
    tem = 0
    for x in l:
        print("x = \n", x)
        # http://thebostonjam.files.wordpress.com/2011/10/nba_g_nbafans_275.jpg" alt
        x = "http://thebostonjam.files.wordpress.com/2011/10/nba_g_nbafans_275.jpg"
        x = re.match(r'http[\w\/\.:_]*jpg', x).group()
        print("x = \n", x)
        tem += 1
        print("urlretrieve(x, '%s.jpg' % tem) = \n", urlretrieve(x, "001_get_tieba_%s.jpg" % tem))
    return res

imgs = getimgs(str(urlread))




