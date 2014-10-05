__author__ = 'John_PC'

# python version:3.41

import urllib.request

from bs4 import BeautifulSoup

page = urllib.request.urlopen("http://www.zhihu.com/question/22935917/answer/23191503")
soup = BeautifulSoup(page)
url = (soup.find_all("div", " zm-editable-content clearfix"))
u = BeautifulSoup(str(url))
print(u.get_text())

f = open("zhihu.txt", "w")
f.write(u.get_text())
f.close()
