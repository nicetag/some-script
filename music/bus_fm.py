# version : 0.3

import urllib.request

from bs4 import BeautifulSoup

vol = input("Enter the vol number : ")
musicurl = "http://luoo.800edu.net/low/luoo/radio"
imgurl = "http://www.luoo.net/music/"
page = urllib.request.urlopen(imgurl + vol)
soup = BeautifulSoup(page)
num = len(soup.select('li[id^="track"]'))


def downloadMusic():
    for i in range(1, 10):
        print(musicurl + vol + "/" + "0" + str(i) + ".mp3")
    for n in range(10, int(num) + 1):
        print(musicurl + vol + "/" + str(n) + ".mp3")


def downloadImg():
    u = str((soup.find_all("img", "vol-cover")))
    print(u[u.find("src") + 5:u.find(">") - 1])
    print()
    input("Done.")


def test():
    downloadMusic()
    downloadImg()


if __name__ == "__main__":
    test()

