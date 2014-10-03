__author__ = 'John_PC'

import urllib

from bs4 import BeautifulSoup

downloadUrl = raw_input("Please input url: ")
downloadUrl = downloadUrl + "?start=0"


def downloadPhoto(url):
    page = urllib.urlopen(url)

    soup = BeautifulSoup(page)
    a = soup.select("div > a > img")
    p = soup.select('a[href*="?start="]')
    for i in range(1, len(a)):
        print(str(a[i]).replace("thumb", "photo")[10:-3])
        url = url + "18"


def pagesNumber(u):
    page = urllib.urlopen(u)

    soup = BeautifulSoup(page)
    a = soup.select("div > a > img")
    p = soup.select('a[href*="?start="]')
    o = -18
    b = []

    for i in range(0, len(p)):
        o = o + 18
        b.append(u + str(o))
    return b


map(downloadPhoto, pagesNumber(downloadUrl))

