from math import sqrt
a = int(input('Enter a number: '))
for i in range(3,int(sqrt(a))):
    if a%i==0:
        print('False')
        break
else:
    print('True')
