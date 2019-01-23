import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}


def getSoup(url):
    count = 0
    flag = True
    while flag and count < 10:
        request = http.request("GET", url, headers=headers)
        if request.status == 200:
            flag = False
        else:
            count += 1
    soup = BeautifulSoup(request.data, "html.parser")
    if len(soup) == 0:
        print("error")
    return soup
