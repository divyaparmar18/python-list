a = [1000,2,5,8,4,99,3,7657,456,666]
x = 0 
y = 0

while y < len(a):
    if x < a[y]:
        x = a[y]
    y =y+1 
a.remove(x)
b = a
x=0
y=0
while y < len(a):
    if x < a[y]:
        x = a[y]
    y =y+1 
print x

a = [1000,2,5,8,4,99,3,7657,456,666]
a.sort()
print a[len(a)-2]

a = [1000,2,5,8,4,99,3,7657,456,666]
b = max(a)
a.remove(b)
c = max(a)
print c









