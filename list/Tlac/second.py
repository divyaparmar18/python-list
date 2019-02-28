#Code likho jo iss list mein se second maximum element (doosra sabse bada element) dhund kar kar print kare.

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0 # index is declared
j = None # variable with none value is taken
k = None # variablew with none value is taken
while i < len(numbers):#condtion is given to run the loop till
    if numbers[i]> j:# conditon is given to chk
        k=j# if upper condtion is ture it will give the value of j to k
        j = numbers[i]# and j becomes the numbers which is on that index of the list
        
    elif  j > numbers[i] > k:# if upper condition is not true here another condition is given to chk weather j is bigger thn number and number is bigger thsn k
        k = numbers[i]# if true the nubmer becomes the numbers index
    i=i+1# increment is done to run the loop
if k == None:# if k is None then k will be j
    k=j# assigned
print k #k is printed 
    