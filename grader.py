score = input("Enter Score: ")
grade=float(score)
if grade > 1.0:
    print('Error value not in range')
elif grade >= 0.9:
    print('A')
elif grade >= 0.8:
    print('B')
elif grade >= 0.7:
    print('C')
elif grade >= 0.6:
    print('D')
elif grade < 0.0:
    print('Error value not in range')
elif grade < 0.6:
    print('F')
