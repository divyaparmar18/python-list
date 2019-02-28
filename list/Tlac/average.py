marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0 # index of the list is defined
while i < len(marks):# condition is given to run the loop till the index is less thn length of the list
    j=0# index of the inner list is defined
    total = 0# total is defined
    while j < len(marks[i]):# condition is given to run the loop till j is less then the length of the inner list
        total = total + marks[i][j]#total is done
        avg = total/len(marks[i])# average is removed by dividing the total marks with the length of the inner list
        j=j+1# increment of the inner list index is done
    i=i+1# increment of the list index is done
    print avg

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]

i=0
while i < len(marks):
    j=0
    total = 0
    while j < len(marks[i]):
        total = total + marks[i][j]
        avg = total/len(marks[i])
        j=j+1
    i=i+1
    print avg

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]

i=0
while i < len(marks):
    j=0
    total = 0
    while j < len(marks[i]):
        total = total + marks[i][j]
        avg = total/len(marks[i])
        j=j+1
    i=i+1
    print avg




