def word_count(str):
    counts = 0
    word = str.split()

    for words in word:
            counts=counts + 1
    return counts 

print word_count('the quick brown fox jumps over the lazy dog.')


def word_count(str):
        counts = 0
        word = str.split(' ')

        for words in word:
                counts =counts+1 
        return counts
print(word_count("the quick brown fox jumps over the lazy dog."))

def word_count(str):
    counts = 0
    word = str.split(' ')

    for words in word:
        counts = counts  + 1
            
    return counts
print(word_count("the quick brown fox jumps over the lazy dog."))

