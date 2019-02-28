
i=0
while i < 1000:
    j=i+1
    while j < 1000:
        k=j+1
        if  i**2 + j**2 == k**2:
            print i,j,k
        k=k+1
        j=j+1
    i=i+1 


i=0
c = 1000
while i<50:
    j=i+1
    while j<50:
        if i**2 + j**2 == c:
            print i,j
        j=j+1
    i=i+1
    