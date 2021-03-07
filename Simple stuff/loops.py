#smallest number with loop
smallest=None
for value in [15,35,86,1,96,-95,-100]:
    if smallest is None: #is, used on None, true/false operations
        smallest=value
    elif value < smallest:
        smallest=value
    print(value,smallest)
print(smallest)
