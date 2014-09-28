__author__ = 'John_PC'

# python version:3.41

import urllib.request

from bs4 import BeautifulSoup

page = urllib.request.urlopen("http://www.douban.com/photos/album/71244874/")
soup = BeautifulSoup(page)

a = (soup.select("div > a > img"))

begin = str(a[1]).find("public") + 7
end = str(a[1]).find(".jpg")

for i in range(1, len(a)):
    print(str(a[i]).replace("thumb", "photo")[10:-3])
