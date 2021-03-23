#A program which reads through mail file and
#looks for the hour in the mails then prints them as counts
#type of line From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#open File
di = dict()
fname = input('Enter file name: ')

try:
    text = open(fname)
except:
    print('File not found')
    quit()

#loop and creation of dictionary
for line in text :
    if line.startswith('From ') :
        line = line.rstrip()
        #print(line)
        line = line.split(' ')
        #print(line)
        hour = line[6].split(':')
        #print(hour)
        hour = hour[0]
        #print(hour)
        di[hour] = di.get(hour, 0) + 1
        #print(di)
#list and sorting
lst = di.items() #If I want to sort normally key,value instead (value,key) i use:
#for hour,value in di.items() :
    #tup = (hour,value)
    #lst.append(tup)
    #print('new',tup)
lst = sorted(lst)
#result
for hour,value in lst :
    print(hour,value)
