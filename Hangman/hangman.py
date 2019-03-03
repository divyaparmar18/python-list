import string
from words import choose_word
from images import IMAGES


# function for letters available user to be used
def available_letters(letters_guessed):
    import string
    all_letters = string.ascii_lowercase
    letters_left = ""
    for letters in all_letters:
        if letters not in letters_guessed:
            letters_left=letters_left + letters
        
    return letters_left


# chk input valid or not
def input_valid_or_not(user_input):
    if len(user_input) != 1:
        return False
    if not user_input.isalpha():
        return False
    else:
        return True


#chk user guessing is correct or not
def is_word_correct(letters_guessed,secret_word):
    if secret_word == chk_word_guessed(secret_word,letters_guessed):
        return True
    else:
        return False

# hint
def giving_hint(secret_word,letters_guessed):
    import random
    not_guessed_letters = []
    index=0
    while index < len(secret_word):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in not_guessed_letters:
                not_guessed_letters.append(letter)
        index=index+1
    return random.choice(not_guessed_letters)

# if letter in secret word
def chk_word_guessed(secret_word,letters_guessed):
    i=0
    word_guessed = ""
    while i<len(secret_word):
        if secret_word[i] in letters_guessed:
            word_guessed=word_guessed+secret_word[i]
        else:
            word_guessed=word_guessed+"_"
        i=i+1
    return word_guessed
# main function
def hangman(secre_word):
    print "Welcome to the HANGMAN GAME !"
    print "I am thinking of a word and the length of the word is " + str(len(secret_word))
    print ""

    letters_guessed = []
    total_lives = remaining_lives = 8
    select_image = [0,1,2,3,4,5,6,7]
# levels to select
    game_level = raw_input("enter the level in which you want to play""\n""for easy level press 'a'""\n""for medium level press 'b'""\n""for hard level press 'c'""\n")
    if game_level == "b":
        total_lives = remaining_lives =6
        select_image = [1,2,3,4,6,7]

    elif game_level == "c":
        total_lives=remaining_lives =4
        select_image = [2,3,5,7] 
    else:
        if game_level != "a":
            print " you didn't choose a correct level so we are taking you to the easy level" 


    while remaining_lives > 0:
        remaining_letters = available_letters(letters_guessed)
        print "The letters which you haven't used yet are :- " + remaining_letters

        guess = raw_input("guess a letter which might be in my word::- ")
        guess_letter = guess.lower()
        if guess_letter == "hint":
            guess_letter = giving_hint(secret_word,letters_guessed)
            print "The letter as a hint which is in secret_word is :-  " + guess_letter
            
        else:
            if (not input_valid_or_not(guess_letter)) and guess_letter != "hint":
                print "Invalid Input"
                continue
        
        if guess_letter in secret_word:
            letters_guessed.append(guess_letter)
            print "Good your guess is correct :- " + chk_word_guessed(secret_word,letters_guessed)
            print ""

            if is_word_correct(letters_guessed,secret_word) == True:
                print "Congtratulations, you won ! * * "
                print ""
                break
        else:
            print "Oops, that letter is not in my word  :-" + chk_word_guessed(secret_word,letters_guessed)
            letters_guessed.append(guess_letter)
            print IMAGES[select_image[total_lives- remaining_lives]]
            remaining_lives=remaining_lives-1
            print "Remaining lives left are " + str(remaining_lives)

    else:
        print "Sorry you loose you were not able to guess the word, the word was " + secret_word

secret_word = choose_word()
hangman(secret_word)

