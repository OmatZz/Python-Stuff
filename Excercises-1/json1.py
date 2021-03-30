#A program to count tags in a webpage parsin json type data
import ssl, re
from urllib.request import urlopen
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Open the url and read the data
url = input('Enter the URL: ')
data = urlopen(url, context=ctx)
data = data.read()
print('Retrieved', len(data), 'characters', 'From:', url)

#print(data.decode())
suma = list()
try:
    js = json.loads(data)
except:
    js = None
#print(json.dumps(js, indent=4))
for item in js['comments'] :
    #print('Count:', item['count'])
    suma.append(int(item['count']))

print('The sum of counts is:',sum(suma))
