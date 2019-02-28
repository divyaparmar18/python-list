list1=[["tina",52],["rina",25],["mahesh",26],["hean",27]]
i=0
j=1
l =len(list1)
a=None
b = None
while i < l-1:
    if a < list1[i][j]:
        b=a
        a = list1[i][j]
    elif  a < list1[i][j] < b:
        b=list1[i][j]
    i=i+1
print b
i=0
count = []
while i < len(list1):
    if b in list1[i]:
        count.append(list1[i])
    i=i+1
new=count
new.sort()
print new
i=0
j=0
while i <len(new):
    print count[i][j]
    i=i+1

