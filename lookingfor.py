# -*- coding: utf-8 -*-

import requests as rq
from bs4 import *
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

def get_num(x):
    s = 0
    for i in x:
        if ord(i) >= ord('0') and ord(i) <= ord('9'):
            s = s*10 + int(i)
    return s

urls = 'https://www.shuquge.com/txt/17604/'
page = rq.get(urls, headers=headers)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, 'lxml')
href = soup.find_all('dd')
href = href[12:]
url = []
for paraurl in href:
    # bookurl = str(paraurl)[13:25]
    bookurl = get_num(str(paraurl)[11:27])
    url.append(bookurl)

num = 0
f = open('./深海提督/深海提督.txt','w',encoding = 'utf-8')
for i in url:
    n_url = urls + str(i) + '.html'
    status_code = 503
    while(status_code!=200):
        page = rq.get(n_url, headers=headers)
        status_code = page.status_code
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, 'lxml')
    title = soup.find('h1').text
    # f = open('./寻找走丢的舰娘/'+title+".txt",'w',encoding = 'utf-8')
    f.write(title+'\n')
    article = soup.find('div', id="content").text
    print(str(num)+' '+title,end = ' ')
    f.write(article)
    f.write('\n\n')
    # f.close()
    print('完成')
    time.sleep(0.01)
    num+=1
	
f.close()
