elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
counter = 0
odd=0
even=0
all_numbers=0
while counter < len(elements):
    all_numbers=all_numbers+1
    if elements[counter] % 2 != 0:
        odd=odd +1
    else:
        even=even+1
    counter=counter+1
print "There are  " +str(odd) + " in the list"
print "There are  " + str(even) + "in the list"
print "There are " + str(all_numbers) + "in the list"

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
counter=0
odd_sum=0
even_sum=0
all_sum = 0
while counter<len(elements):
    all_sum=all_sum+elements[counter]
    if elements[counter] % 2 != 0:
        odd_sum=odd_sum+elements[counter]
    else:
        even_sum=even_sum+elements[counter]
    counter=counter+1
print "The sum of the all odd numbers in the list is  " + str(odd_sum)
print "The sum of all the even numbers in the list is  " + str(even_sum)
print "The sum of all the numbers in the list is " + str(all_numbers)

odd_avg = odd_sum/odd
even_avg = even_sum/even
all_avg = all_sum/all_numbers
print "The average of the odd numbers in the list is " + str(odd_avg)
print "The average of the even numbers in the list is  " + str(even_avg)
print "The average of all the numbers in the list is " + str(all_avg)