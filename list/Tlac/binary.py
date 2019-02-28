
binary_number =  [1, 0, 0, 1, 1, 0, 1, 1]
i=0 
j=0
k=0
total = 0
l = len(binary_number)
while i < l:#condition is givne
    if binary_number[i] != 1 and binary_number[i] != 0:# chk weather it is a binary or not
        print "Not a valid list"
        break# if not bianry break it
    elif binary_number[l-1] == 0:#if it is a binary and the nubmer in the list is 0 then it will remain 0
        j=0
    else:# if not 0
        j = 2**k#we will use the exponent
        total = total+j# total will be total of total and j
    l=l-1# len is decreased
    k=k+1#k is increased
print total# total is printed



