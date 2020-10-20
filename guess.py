import random
from math import *

# this program looks for a secret word. You only get 3 try's.
secrete_word = "monkey"
guess = ""
guess_limit = 3
attempts = 0
out_of_guesses = False


while guess != secrete_word and not (out_of_guesses):
    if attempts < guess_limit:
        guess = input("Enter the secrete word please: ")
        attempts += 1
    else:
        out_of_guesses = True


if out_of_guesses and guess != secrete_word:
    print("Out of guesses, you loose!")
else:
    print("you win!")








