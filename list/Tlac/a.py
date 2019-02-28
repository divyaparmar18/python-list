numbers=[50, 40, 2, 70, 5, 12, 5, 10, 7]
index=0#here we gave the index of the list
first_min , sec_min = numbers[index],None# here we took two variables in which we stroed the first and sec minimum so first is first element of the list and second is none
while index<len(numbers)-1:# here we run the loop till length of the list is less
    if first_min > numbers[index+1]:#here we give the condition that weather first number is greater or no
        first_min  , sec_min = numbers[index+1] , first_min#if upper conditon is true first min will become the second element of the list and second fir take the value of first
    elif first_min<numbers[index+1]<sec_min:# here we give another condition that if first sunber is smaller and list number is smaller than second then second will become list elemnet
        sec_min=numbers[index+1]# sec min will become list element
    elif sec_min == None:# here we give edge cases that if sec minimum is none then second element is second_minimum  
        sec_min = numbers[index+1]
    index=index+1# increment is done
print sec_min
