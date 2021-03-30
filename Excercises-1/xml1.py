#A program to count tags in a webpage parsin xml type data
import ssl, re
from urllib.request import urlopen
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Open the url and read the data
url = input('Enter the URL: ')
data = urlopen(url, context=ctx)
data = data.read()
print('Retrieved', len(data), 'characters')

#print(data.decode())
suma = list()
tree = ET.fromstring(data)
lst = tree.findall('.//comment')
for count in lst :
    #print('Count:', count.find('count').text)
    suma.append(int(count.find('count').text))
#print(lst)
print('Count:',len(lst),'\n', 'Sum:', sum(suma)) #result
