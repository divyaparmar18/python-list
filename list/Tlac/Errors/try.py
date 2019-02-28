def second_minimum(number):
  i=0
  x=number[i]
  while i < len(number)-1:
    if x > number[i+1]:
      x = number[i+1]
    i=i+1
  number.remove(x)
  b = number
  i=0
  x = b[i]
  while i < len(b)-1:
    if x > b[i+1]:
      x = b[i+1]
    i=i+1
  return x

print(second_minimum([70, 50, 20, 23, 40]))
print(second_minimum([70, 50, 10, 2, 40]))

