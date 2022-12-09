# prompt used: make a python script that asks the user to input length of password and which symbols to use and append the password to a file

import random
import string
import os

# Set the default character set for the password
default_characters = string.ascii_letters + string.digits + string.punctuation

# Ask the user for the length of the password
password_length = int(input('Enter the length of the password: '))

# Ask the user which symbols to use for the password
symbols = input('Enter the symbols to use for the password (leave blank for default): ')
if symbols == '':
    # Use the default character set if no symbols are specified
    characters = default_characters
else:
    # Use the specified symbols for the password
    characters = symbols

# Generate the password
password = ''.join(random.choices(characters, k=password_length))

# Append the password to the file
with open('passwords.txt', 'a') as file:
    file.write(password + '\n')

# Print the password
print(password)
