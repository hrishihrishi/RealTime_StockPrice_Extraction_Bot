# -*- coding: utf-8 -*-
"""RealTime_StockPrice_Extraction_Bot.py"""

import requests
from bs4 import BeautifulSoup
import time

ticker=input("enter stock name:").upper()
exchange=input("enter exchange (NSE/BOM):").upper()
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'


def fetchAndSavefile(url,path):
  r = requests.get(url)
  with open(path, 'w') as f:
    f.write(r.text)

fetchAndSavefile(url, 'webscraped.html')

with open('webscraped.html', 'r') as f:
    html_content = f.read()
for i in range(3):
  soup = BeautifulSoup(html_content, 'html.parser')
  price = float(soup.find(class_="YMlKec fxKbKc").text.strip()[1:].replace(",",""))
  print(price)
  time.sleep(2)
