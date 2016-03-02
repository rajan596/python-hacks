# python 3.5

import urllib.request
import urllib.parse
import re

url="http://www.mathsisfun.com/numbers/fibonacci-sequence.html"
wp=urllib.request.urlopen(url)

# print whole fetched page
print(wp.read())


