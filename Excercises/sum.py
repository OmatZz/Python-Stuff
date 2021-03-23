#read through and parse a file with text and numbers.
# extract all the numbers in the file and compute the sum of the numbers.

#open file
import re
fhandle = input('Enter file name: ')
ftext = open(fhandle)

numlst = list()
for line in ftext :
    line.rstrip()
    y = re.findall('[0-9]+' , line) #search for any numbers
    for val in y :
        number = int(val)
        numlst.append(number)
        #print(number)

print('Sum :',sum(numlst))
