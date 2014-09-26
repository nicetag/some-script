# version : 0.2
import urllib.request

from bs4 import BeautifulSoup


def bus_fm():
    vol, num = input("Enter the vol and num: ").split()
    musicurl = "http://luoo.800edu.net/low/luoo/radio"
    imgurl = "http://www.luoo.net/music/"
    for i in range(1, 10):
        print(musicurl + vol + "/" + "0" + str(i) + ".mp3")
        str((musicurl + vol + "/" + "0" + str(i) + ".mp3"))
    for n in range(10, int(num) + 1):
        print(musicurl + str(vol) + "/" + str(n) + ".mp3")
    page = urllib.request.urlopen(imgurl + vol)
    soup = BeautifulSoup(page)

    u = str((soup.find_all("img", "vol-cover")))
    print(u[u.find("src") + 5:u.find(">") - 1])
    print()
    input("Done.")


def test():
    bus_fm()


if __name__ == "__main__":
    test()

