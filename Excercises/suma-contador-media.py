num = 0
total = 0.0

while True:
    sval = input('Enter a number and type done when finished: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Bad input')
        continue
    #print(fval)
    num = num + 1
    total = total + fval

#print('All done')
print('Sum of numbers:',total,'Total of numbers:',num,'Mean:', total/num)
