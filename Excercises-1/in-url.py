#program to retrieve the link from a consecutive order
#the order is assigned by the user
#the last link is the one to print
import ssl, re
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL: ')
count = input('Enter count: ')
position = input('Enter position: ')
count = int(count)
position = int(position)

while True :
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    lsturl = list()

    for tag in tags :
        #print(tag.get('href', None))
        turl = tag.get('href', None)
        lsturl.append(turl)
    #print(lsturl)
    url = lsturl[position - 1]
    print(url)
    lsturl.clear()
    count = count - 1
    if count > 0 :
        position = input('Enter position: ')
        print('New position: ',position)
        position = int(position)
        continue
    if count <= 0 :
        break

print('Done, the last URL is:',url)
