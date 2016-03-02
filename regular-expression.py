# python3

'''
Identifiers :
\d : any number
\D : anything but a number
\s : space
\S : anything but a space
\w : any character
\W : anything but a character
.  : any character, except new line
\b : white space
\. : a period

Modifiers :
{1-3} : \d{1,3}
+  : match 1 or more
?  : match 0 or 1
*  : match 0 or more
$  : match end of a string
^  : match begining of a string
|  : either or
[] : range or "varience" [A-Za-z0-9]
{x}: expecting x amount

White Space Characters :
\n : new line
\s : space
\t : tab
\e : escape
\f : form feed
\r return

'''
import re

s='''
hello
This is example18 string to test 15 Regular Expression,
So Keep watching 1996
'''

nos=re.findall(r'\d{1-4}',s)
capital=re.findall(r'[A-Z][a-z]*',s)
year=re.findall(r'\d{4}',s)

print(nos)
print(capital)
print(year)





