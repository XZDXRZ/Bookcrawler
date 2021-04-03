# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:25:58 2021

@author: XZDXRZ
"""

import requests as rq
from bs4 import BeautifulSoup

url = 'http://www.shuquge.com/txt/73804/'
page = rq.get(url)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, 'lxml')
href = soup.find_all('dd')
print(href[12:])