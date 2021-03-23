#8.4 Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list
#and if not append it to the list. When the program completes,
#sort and print the resulting words in alphabetical order.


#open list and read text file

file = input('Enter file name: ')
ftext = open(file)
lst = list()

#loop

for line in ftext :
    line = line.rstrip()
    words = line.split()
    for word in words :
        word = str(word)
        if not word in lst :
            lst.append(word)

print(sorted(lst))
