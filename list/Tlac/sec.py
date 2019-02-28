name = [1,3,4,56,7]
first,second = None,None
for n in name:
    if n > first:
        first,second = n,first
    elif first > n > second:
        second = n
        if second == None:
            print first
print second

list1 = [34,55,45,32,80]
max = None

for n in list1:
    if n > max:
        max = n 
print max

