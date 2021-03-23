#Listar el top 10 de palabras mas usadas de un archivo

#open File
fname = input('Enter file name: ')
try :
    text = open(fname)
except:
    print('File not found')
    quit()

di = dict()
#loop and dictionary
for line in text :
    line = line.strip()
    line = line.split()
    for words in line :
        di[words] = di.get(words, 0) + 1

#sorted tuple
tup = list()
for word,value in di.items() :
    newtup = (value,word)
    tup.append(newtup)
    #print(tup)
tup = sorted(tup, reverse=True)
#print(tup[ : 10])
for value,word in tup[:10] : #top 10 words most used
    print(word,value)
