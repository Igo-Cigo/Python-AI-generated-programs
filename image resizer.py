import os
from PIL import Image

# get the dimensions from the user
width = input("Enter the width of the image: ")
height = input("Enter the height of the image: ")

# get the list of files in the current directory
files = os.listdir()

# ask the user to select an image
for i, file in enumerate(files):
    print(f"{i}: {file}")

selected = input("Enter the number of the image you want to resize: ")
selected_file = files[int(selected)]

# open the selected image and resize it
img = Image.open(selected_file)
img = img.resize((int(width), int(height)))

# save the resized image
img.save(f"resized_{selected_file}")
