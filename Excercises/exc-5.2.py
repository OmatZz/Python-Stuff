largest = None
smallest = None
count = 0
sum = 0

while True:
    num = input('Enter a number: ')

    if num == 'done':
        break

    try:
        fnum = float(num)

    except:
        print('Invalid Input')
        continue
    if largest is None :
        largest = fnum
    if largest < fnum :
        largest = fnum
    if smallest is None :
        smallest = fnum
    if fnum < smallest :
        smallest = fnum
    count = count + 1
    count = count + 1
    sum = sum + fnum

print('Maximum',largest)
print('Minimun',smallest)
print('Mean', sum/count)
