# -*- Coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url = "https://tenki.jp/lite/forecast/3/16/4410/13113/"
r = requests.get(url)
bsObj = BeautifulSoup(r.content, "html.parser")
#天気を取得
we = bsObj.find(class_="weather-telop")
weth = we.get_text()
#最高気温を取得
hig = bsObj.find(class_="high-temp temp")
high = hig.get_text()
#最低気温を取得
lo = bsObj.find(class_="low-temp temp")
low = lo.get_text()
