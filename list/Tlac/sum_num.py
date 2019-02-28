number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
l=len(n)
list1 = []
while i < (l):# condition is given to run the loop till the length of n 
    k=i+1# here we took a number to get the all the numbers from the list to be chked from all the nubmerd
    while k < l:# condition is givne to run the loop
        if  n[i] + n[k] == number:# here we chk weather the thing we have to chk is yes or no
            list1.append([n[i],n[k]])# here we append those number in the empty list whose sum is 30
        k=k+1# we did the increment
    i=i+1# we did the increment
if list1 == []:# here we have to chk weather list is empty or not
    print "There are no numbers in the list whose sum is number"
else:
    print list1

 