# version : 0.1

import urllib.request

from bs4 import BeautifulSoup


page = urllib.request.urlopen("http://www.yayaxz.com/resource/24272")
soup = BeautifulSoup(page)
url = soup.select('a[href^="ed2k"]')
begin = "ed2k"
end = "target"
b = str(url)
print(b[b.find(begin):b.find(end) - 2])
