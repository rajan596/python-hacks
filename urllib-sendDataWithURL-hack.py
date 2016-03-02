import urllib.request
import urllib.parse

url="https://www.codechef.com/"

values={
    'username':'rtkasodariya',
    'password':'password'
}

# encode data
data=urllib.parse.urlencode(values)
data=data.encode('ascii')

# finally Request
req=urllib.request.Request(url,data)
try:
    response=urllib.request.urlopen(req)
    print("successfully logged in")
    #print(response.read())
    print('rtkasodariya' in response)
except urllib.error.URLError as e:
    print(e.reason)
    print(e.code)

