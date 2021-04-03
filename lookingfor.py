# -*- coding: utf-8 -*-

import requests as rq
from bs4 import BeautifulSoup

url = 'http://www.shuquge.com/txt/73804/'
page = rq.get(url)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, 'lxml')
href = soup.find_all('dd')
href = href[12:]
url = []
for paraurl in href:
    bookurl = str(paraurl)[13:26]
    url.append(bookurl)

rooturl =  'http://www.shuquge.com/txt/73804/'
for i in url:
    n_url = rooturl + i
    #print(n_url)
    page = rq.get(n_url)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, 'lxml')
    title = soup.find('h1').text
    f = open('./寻找走丢的舰娘/'+title+".txt",'w',encoding = 'utf-8')
    f.write(title+'\n')
    article = soup.find('div', class_ = 'showtxt').text
    print(title,end = ' ')
    f.write(article)
    f.close()
    print('完成')