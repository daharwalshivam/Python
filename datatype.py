x = input()
j = 0
try:
    y = int(x)
    j = 2
    if j == 2:
        print('Integer type')
except:
    for i in x:
        if i == '.':
            j = 1

if j == 1:
    print('float type')
elif j == 0:
    print('string type')
