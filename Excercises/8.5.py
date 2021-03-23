#8.5 Open the file mbox-short.txt and read it line by line.
#When you find a line that starts with 'From '
#You will parse the From line using split()
#and print out the second word in the line
# Then print out a count at the end.


#opening the file
while True:
    fname = input('Enter the file name: ')
    try:
        ftext = open(fname)
    except:
        print('File not found')
        break

    count = 0

    for line in ftext :
        line = line.rstrip()
        if line.startswith('From ') :
            line = line.split()
            print(line[1])
            count = count + 1
    print("There were", count, "lines in the file with From as the first word")
