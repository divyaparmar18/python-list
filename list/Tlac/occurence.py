char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
counter=0
list_elements = []
while counter< len(char_list):
    list_single_elements = []
    if char_list[counter] not in list_single_elements:
        list_single_elements.append(char_list[counter]) 
        list_single_elements.append(char_list.count(char_list[counter]))
        if list_single_elements not in list_elements:
            list_elements.append(list_single_elements)
    counter=counter+1
print list_elements
if list_elements!= []:
   index=0
   while index < len(list_elements):
       print str(list_elements[index][0]) + " - " + str(list_elements[index][1]) + " times"
       index=index+1


