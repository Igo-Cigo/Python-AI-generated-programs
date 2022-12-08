# The program is very slow and kinda broken, wouldn't recommend using

import itertools

# Ask the user for input
letters = input('Enter some letters: ')

# Load a list of words from the dictionary
with open('words.txt') as f:
    words = [line.strip() for line in f]

# Get all possible combinations of the letters
combinations = itertools.permutations(letters)

# Check if any of the combinations match a word in the dictionary
for combination in combinations:
    word = ''.join(combination)
    if word in words:
        print(f'Found word: {word}')
        break
else:
    print('No words found')
