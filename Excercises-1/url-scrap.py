#program to retrieve al the numbers from a page and sum it all
import ssl, re
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup)
# Retrieve all of the anchor tags
numlist = list()
tags = soup('span')
for tag in tags:
     #Look at the parts of a tag
    print('TAG:', tag)
    number = re.findall('[0-9]+', tag.decode()) #extract the numbers
    for number in tag :
        print(number)
        numlist.append(int(number))

print(sum(numlist))
 #for tag in tags
