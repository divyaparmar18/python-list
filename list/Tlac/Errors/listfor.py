num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)

num = 10
zero_list = [ i%1 for i in range(num)]
print(zero_list)


num = 10
zero_list = [ i%1 for i in range(1,num)]
print(zero_list)

num = 9876542345
string_wali_num =  str(num)
ek_nayi_list = [int(i) for i in string_wali_num]
print(ek_nayi_list)

def word_count(str):
  new_list = [i for i in str if i == ' ']
  sum = 0
  for i in new_list:
    sum=sum+1 
  return sum
print(word_count(""" the quick brown fox jumps over the lazy dog."""))

