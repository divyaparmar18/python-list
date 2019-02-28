m = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]]
# finding the diagnol sum
i=0
j=len(m)-1
diag=0
while i<len(m):
    diag=diag+  m[i][j]
    j=j-1
    i=i+1
#finding the another diagnol
i=0
j=0
calcu=0
while i<len(m):
    calcu=calcu+m[i][j]
    j=j+1
    i=i+1
#sum of horizontal and vertical is done
i=0
sumtotal=None
while i < len(m):
    j=0
    sum=0
    total = 0
    while j<len(m[i]):
        total=total+m[j][i]
        sum=sum+ m[i][j]
        j=j+1
    if sum != total:
        break
    i=i+1
# it is checked the weather all are equal or not
if sum != total != calcu != diag:
    print "It's not a magic square"
else:
    print "It's a magic square"