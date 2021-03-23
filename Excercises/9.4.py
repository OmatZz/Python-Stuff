# 9.4 Write a program to read through the mbox-short.txt
#and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word
#of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps
#the sender's mail address to a count of the number of times
#they appear in the file. After the dictionary is produced,
#the program reads through the dictionary using a maximum loop
#to find the most prolific committer.

#open the file
nfile = input('Enter the file name: ')
mails = dict()
try:
    ftext = open(nfile)
except:
    print('File not found')
    quit()
#loop
for line in ftext :
    if line.startswith('From ') :
        #print(line)
        line = line.split()
        #print(line[1])
        mail = line[1]
        mails[mail] = mails.get(mail, 0) + 1
#maximum loop
mcount = None
mmail = None
for mail,count in mails.items() :
    if mcount is None or count > mcount :
        mmail = mail
        mcount = count
#result
print('The address with more mails is:\n',mmail,'\n''With:\n',mcount,'mails')
