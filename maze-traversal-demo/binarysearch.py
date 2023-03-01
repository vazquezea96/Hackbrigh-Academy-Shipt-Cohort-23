"""
Binary search.

Guesses random number from 1 to 100 using a binary
search method.

This is the most efficient way to guess this number.
"""

import random

def play_game():

    secret_number = random.randint(1, 100)
    guess = None
    too_low = 0
    too_high = 101

    print(f"Shh... the secret number is {secret_number}")

    while secret_number != guess:
        guess = int((too_high + too_low) / 2)
        print(f"Too High = {too_high}, Too Low = {too_low}, Guess = {guess}")

        if guess > secret_number:
            too_high = guess
        if guess < secret_number:
            too_low = guess
