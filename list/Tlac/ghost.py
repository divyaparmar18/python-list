ghost_list=[[0,2,0,4,7,9],
   [8,0,11,3,8,0],
   [23,0,0,0,3,2],
   [17,44,6,80,0,6],
   [2,56,0,3,0,2],
   [3,0,8,4,6,3,]]
index=0
sum = 0
while index < len(ghost_list):
    counter=0
    while counter < len(ghost_list)-2:
        if counter == 0 and ghost_list[counter+1][index] != 0 and ghost_list[counter][index]!=0:
            sum=sum+ ghost_list[counter][index]
        if ghost_list[counter][index] != 0 and ghost_list[counter+2][index] != 0 and ghost_list[counter+1][index] != 0:
            sum=sum+ ghost_list[counter+1][index]
        if counter == len(ghost_list)-3 and ghost_list[counter+1][index] != 0 and ghost_list[counter+2][index]!= 0:
            sum=sum+ ghost_list[counter+2][index]
        counter=counter+1
    index=index+1
print sum
    