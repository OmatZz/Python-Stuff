#introduce any number and express if it is bigger than 10
num=input('What is your number? ')
try:
    inum=int(num)
except:
    inum='not a number'
    print('A number pls ')
num=input('... your number? ')
inum=int(num)
if inum > 10:
    print('Your number is bigger than 10')
if inum < 10:
    print('Your number is less than 10')
print('Fin')
