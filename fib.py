a = -1
b = 1
n = int(input('enter the value of n: '))
while n != 0:
    print(a+b)
    a,b=b,a+b
    n = n-1
