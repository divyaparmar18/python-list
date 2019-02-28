marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0 # index of the list is declared
total = 0# took a variable to get the total
while i < len(marks):# condition is given to run the loop 
    j=0 # index of the inner list is declared 
    while j < len(marks[i]):# condition is given to run the loop
        total = total + marks[i][j] # total is been done
        j=j+1# increment is done
    i=i+1 # increment is done
print total 



    

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]

i=0
total = 0
while i < len(marks):
    j=0
    while j < len(marks[i]):
        total = total + marks[i][j]
        j=j+1
    i=i+1
print total

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]

i=0
total = 0
while i < len(marks):
    j=0
    while j < len(marks[i]):
        total = total + marks[i][j]
        j=j+1
    i=i+1
print total



    