n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
index=0# index is given
duplicate =[]# empty list is declared
while index<len(n):#condition is given
    counter=index+1# here  we declared another index
    while counter< len(n):# here we give the condiiton
        if n[index] == n[counter]:#  here we chk the similar one
            duplicate.append(n[counter])# here we append the same number in new list
            del (n[counter])#n we deleted the duplicate one
            counter=counter# if upper condition is true then counter wont increse
        else:
            counter=counter+1# if upper condition is not true increment is done
    index=index+1# index is incremented
print n# list of uniq is printed
print duplicate# list of duplicate is printed