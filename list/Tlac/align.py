width = 8
i=1
j=0
k=3
while i < width:
    while j <i:
        print " "* (width-i) + i*'h'+j*'h'
        j=j+1
    i=i+1
i=0
while i<width:
    print ' '*k + "h" * width+' '.ljust(width,' ')+"h"*width
    i=i+1
i=0
width = 5
while i < k:
    print " " * 2 + "h" * width*(width)
    i=i+1

width = 8
i=0
while i<width:
    print ' '*k + "h" * width+' '.ljust(width,' ')+"h"*width
    i=i+1


