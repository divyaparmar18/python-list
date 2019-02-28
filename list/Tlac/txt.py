l=[[0,2,0,4,7,9],
   [8,0,11,3,8,0],
   [23,0,0,0,3,2],
   [17,44,6,80,0,6],
   [2,56,0,3,0,2],
   [3,0,8,4,6,3]]
i=0
sum = 0
while i < len(l):
    k=0
    while k < len(l)-2:
        if k == 0 and l[k+1][i] != 0 and l[k][i]!=0:
            sum=sum+ l[k][i]
        if l[k][i] != 0 and l[k+2][i] != 0 and l[k+1][i] != 0:
            sum=sum+ l[k+1][i]
        if k == len(l)-3 and l[k+1][i] != 0 and l[k+2][i]!= 0:
            sum=sum+ l[k+2][i]
        k=k+1
    i=i+1
print sum
    