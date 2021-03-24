#the library which does all the socket connection
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://url.com')

for line in fhand :
    print(line.decode().strip())
