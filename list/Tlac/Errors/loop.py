
for i in range (1,200):
	number = i
	result = 0
	digit = number % 10
	result = result + (digit**3)
	number = number/10
        if i == result:
            print i

dict = { "Name": "zeba", "Age": 7, "Name": "mann1"}
print dict[0] 
