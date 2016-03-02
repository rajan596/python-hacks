# pythin 3
# urllib module

import urllib.request
import urllib.parse
import re

'''
content=urllib.request.urlopen('http://www.google.com/')

# read whole content fetched by URL request
# print(content.read())

url='http://pythonprogramming.net'
values={
        's':'basic',
        'submit':'search'
    }

# encode data in URL
# exa : www.google.com/?search=query

data=urllib.parse.urlencode(values)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
response=urllib.request.urlopen(req )
content=response.read()

#print(content)
print(response)

'''
try:
    url='https://www.google.com/search?q=codeforces'

    headers={}
    headers['User-Agent']='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
    req=urllib.request.Request(url,headers=headers)
    res=urllib.request.urlopen(req)
    content=res.read()

    # parse links : <a href="vd"> link </a>
    capitals=re.findall(r'[A-Z][a-zA-Z0-9]{4}[ ]',str(content))  

    for c in capitals:
        print(c)
    
    file=open('fetched_links.txt','w')
    file.write(str(content))
    file.close()
    
except Exception as e:
    print(e)
