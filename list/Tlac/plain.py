name=[ 'n', 'i', 't', 'i', 'n' ]

i = 0
l=len(name)# length function is used
name1 = []#empty list is taken for a new list to be formed
while i < l:#condtion is given to run the loop till length for the list
    name1.append(name[l-1])# we have used append function to append the answer
    l=l-1# here we have used decrement of the length
print name1# it will print the new list
if name == name1:#here we chk weather both the list are same or no
    print "its a plaindrome"# if upper condition is true this is printed
else:# if not upper condition
    "print itd not a plaindrome"# this is printed