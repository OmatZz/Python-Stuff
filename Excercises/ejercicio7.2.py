# Write a program that prompts for a file name,
#then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

fname = input('Enter file name: ')
fhandle = open(fname)
count = 0
total = 0
#looking part
for line in fhandle :
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:') :
        count = count + 1
        find = line.find(':')
        number = line[find+1:]
        fnumber = float(number)
        total = total + fnumber

#the average is the quotient between the total(sum of )and the count(number of lines)
print('Average spam confidence:',total/count)
