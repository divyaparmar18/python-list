#Code likho jo iss list mein se second maximum element (doosra sabse bada element) dhund kar kar print kare.

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0 # index is defined
j=None # a variable with none is taken
while i < len(numbers):# loop is ran
    if numbers[i] > j:# condition is given to chk weather the number is big or no
        j=numbers[i]# if condition true j is given a new value
    i=i+1# increment is done
print j# largest nubmer is printed