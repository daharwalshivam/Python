x = int(input('Enter a number '))
a = 0
for i in range(1,10000):
    if x%i == 0:
        a = a + i
a = a - x
if x == a:
    print('Perfect number')
else:
    print('It is not a perfect number')
