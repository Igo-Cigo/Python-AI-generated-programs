#prompt used: Make a python script that turns a selected image into ascii art

# To use this script, save it to a file (e.g. ascii_art.py) and run it from the command line with the name of the image file you want to convert as the argument, like this:

# python ascii_art.py my_image.jpg
# This will print the ascii art version of the image to the console. You can redirect the output to a file if you want to save it, like this:

# python ascii_art.py my_image.jpg > my_ascii_art.txt

# Import the necessary libraries
import argparse
import numpy as np
from PIL import Image

# Create a new argument parser
parser = argparse.ArgumentParser()

# Add an argument for the image file
parser.add_argument('image_file', help='The image file to convert to ascii art')

# Parse the arguments
args = parser.parse_args()

# Open the image file
image = Image.open(args.image_file)

# Convert the image to grayscale
gray_image = image.convert('L')

# Resize the image
resized_image = gray_image.resize((80, 40))

# Create a numpy array from the image data
image_data = np.array(resized_image)

# Map the pixel values to ascii characters
chars = np.array(list('@B%8WM#*oahkbdpwmZO0QJQXzcvnxrjft/\|()1{}[]-_+~<>i!lI;:,"^`\'. '))
scaled_image_data = (255.0 / image_data.max() * (image_data - image_data.min())).astype(np.uint8)

# Make sure the values in scaled_image_data are within the bounds of chars
scaled_image_data = np.minimum(scaled_image_data, len(chars) - 1)
scaled_image_data = np.maximum(scaled_image_data, 0)

ascii_image = chars[scaled_image_data]

# Print the ascii image
for row in ascii_image:
    print(''.join(row))
