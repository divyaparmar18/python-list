list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i = 0
l = len (list1)
list3 = []
while i < l:# condition is given
    if list1[i] not in list2:# it will chk weather the element is there in list or no
        list3.append(list1[i])#  if the condition is true it will append
    i=i+1# increment is done
if list3 == []:# it will chk weather the list is empty or no
    print "all elements are there"# if upper condtion is true it will be printed
else:# if upper condition not true
    print list3# new list is printed

    