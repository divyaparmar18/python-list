l = [8,2,0,6,9,1]
i=0
while i < len(l)-2:
    if i == 0 and l[i+1] != 0:
            print l[i]
    if l[i] != 0 and l[i+2] != 0 and l[i+1] != 0:
        print l[i+1]
    if i == len(l)-3 and l[i+1] != 0:
        print l[i+2]
    i=i+1     