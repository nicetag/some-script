# python version:2.78

import urllib.request

from bs4 import BeautifulSoup

page = urllib.request.urlopen("http://www.yayaxz.com/resource/32890")
soup = BeautifulSoup(page)
a = soup.select('a[href^="ed2k"]')

d = "ed2k"
e = "target"

b = str(a)
print(b[b.find(d):b.find(e) - 2])
