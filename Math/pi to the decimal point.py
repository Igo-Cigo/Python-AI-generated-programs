# prompt used: Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go. This should be a python script

import math

# Prompt the user to enter the number of decimal places
decimal_places = int(input("Enter the number of decimal places: "))

# Use the format() function to print the value of PI to the specified number of decimal places
print("The value of PI to {} decimal places is: {:.{}f}".format(decimal_places, math.pi, decimal_places))
