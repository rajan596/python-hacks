# python3

import urllib.request
from bs4 import BeautifulSoup
import re

url='http://www.geeksforgeeks.org/'
header={}

req=urllib.request.Request(url,headers=header)
data=urllib.request.urlopen(req).read()

#print(data)

soup=BeautifulSoup(data)
#print(type(soup))

#print(soup.prettify()[0:1000])
'''
links=soup.find_all("a")
print(links)

for link in links:
    print(link.get('href'))
    #print(link)

'''

#print(soup.title)
#print(soup.header)
#print(soup.get_text())

posts=soup.find_all(rel="bookmark")

for post in posts:
    print(post.get("href"))
