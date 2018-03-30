x,y = input().split()
x = int(x)
y = int(y)
a = 0

for i in range(1,10000):
    if x%i == 0 and y%i == 0 :
        a = a + 1
    else:
        a = a
print(a)
