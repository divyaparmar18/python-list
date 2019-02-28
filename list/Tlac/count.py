#Code likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai unhe count kare. Aur firr unka count print kare.

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0#we declared the index
j=0#took a variable to count the numbers
while i < len(numbers):#gave condition to run the loop till length
    if numbers[i] > 20 and numbers[i] < 40:#chk the condition given
        j=j+1#if upper condition is ture increment will be done
    i=i+1# index of the list increment
print j#result of numbers is printed