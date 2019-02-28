mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
new = mainStr.split(" ")# this will split the string

i=0
while i<len(new):
    if new[i] == subStr:
        new.remove(new[i])
    i=i+1
print " ".join(new)

mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
new = mainStr.split(" ")
replacementStr = "on"
i=0
while i<len(new):
    if new[i] == subStr:
        new[i] = replacementStr
    i=i+1
print  " ".join(new)


