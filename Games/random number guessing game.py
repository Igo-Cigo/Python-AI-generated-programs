# prompt used: make a python random number guessing game

import random

# Generate a random number between 1 and 100
target = random.randint(1, 100)

# Set the number of guesses to 0
num_guesses = 0

# Prompt the user to guess the number
guess = int(input('Guess a number between 1 and 100: '))

# Keep prompting the user until they guess the correct number
while guess != target:
    # Increment the number of guesses
    num_guesses += 1

    # Check if the guess is too high or too low
    if guess > target:
        print('Your guess is too high')
    else:
        print('Your guess is too low')

    # Prompt the user for another guess
    guess = int(input('Guess again: '))

# Print a success message
print(f'You guessed the number in {num_guesses} tries!')
