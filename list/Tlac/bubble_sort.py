numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
running=0# here we start the counting of how much time sorting will be done
while running < len(numbers):#here we give the condition to run the loop till when
    index=0# here we declare the index of the list
    while index<len(numbers)-1:# here we give the condiiton to run the loop in the list
        if numbers[index]>numbers[index+1]:# here we check that if the first number is bigger thn second
            numbers[index],numbers[index+1] = numbers[index+1],numbers[index]# so if the condition is true it will swap the nubmers
        index=index+1# here we do the increment of the index 
    running=running+1# the number of times the loop will be done and sorting will be done is increasing
print numbers# final sorted list is printed


numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
running_=0# here we start the counting of how much time sorting will be done
while running < len(numbers):#here we give the condition to run the loop till when
    index=0# here we declare the index of the list
    while index<len(numbers)-1:# here we give the condiiton to run the loop in the list
        if numbers[index]<numbers[index+1]:# here we check that if the first number is bigger thn second
            numbers[index],numbers[index+1] = numbers[index+1],numbers[index]# so if the condition is true it will swap the nubmers
        index=index+1# here we do the increment of the index 
    running=running+1# the number of times the loop will be done and sorting will be done is increasing
print numbers# final sorted list is printed
