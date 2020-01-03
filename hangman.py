#list of words i want to use, i know some of it is weird.
words= ["person", "life", "hate", "jello","taco","weasel","monkey","america","toxic","depression"]
#the import random will do as it says, randomize the words so it just doesnt stay to one word.
#for example it wont stay on person, everytime you try, itll pick a random word for you to guess.
import random
#will pick the words randomly and will put it into an empty fucntion and will hide it until its guessed.
secret_word=random.choice(words)
#the dashes will be the legth of the word that is randomized, if its hate, it will put in 4 dashes for how long the word is.
dashes = "-" * len(secret_word)
#amount of tries you have left, i wanted to be semi-fair so i put 15 tries to guess the letter or word correctly.
tries_left = 15
#creates a function in order to get the  guess or letter, such as asking what the letter is and the user putting in an input for that letter.
#The letter has to be a lowercase letter as well, if its upercase it will simply ask for to change that letter to lowercase.
def get_guess():
#put in a while loop to keep asking the letter until you guess the word or you put in the wrong input such as having more than one letter or an uppercase.
    while True:
#the amount of guesses is the amount of times you have to put in a letter.
        guess = input("What is the letter: ")
        if len(guess) != 1:
            print "Your can only have one letter"
        elif not guess.islower():
            print "It has to be lowercase not capital you baboon"
        else:
            return guess
#updates the dashes with the implemented letter that was given by the user such as "a" or "b" and so on.
def update_dashes(word, dashes, guess):
    for i in range(len(word)):
        if word[i] == guess:
            dashes = dashes[:i] + guess + dashes[i + 1:]
    return dashes
#shows how many tries you have and the amount of tries you taken.
while tries_left > 0 and dashes != secret_word:
    print dashes
    print str(tries_left) + " Chances left:"
    guess = get_guess()
    dashes = update_dashes(secret_word, dashes, guess)
    if guess in secret_word:
        print "That letter is there already you bean"
    else:
        print "That letter isnt there put in another letter"
        tries_left = tries_left - 1
if tries_left == 0:
#if you guess right it you win, horray good for you. You want a cookie. if you dont get it right you lose, so no cookie.
    print "Rip the answer was: " + secret_word + " You lose. Your bad. HAHA get good."
else:
    print "The word was: " + secret_word+ " You win."
