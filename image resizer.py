# Self explanitory, the script only works for .jpg and .png files, if you want to add yours edit the code at line 13

import os
from PIL import Image

# get the dimensions from the user
width = input("Enter the width of the image: ")
height = input("Enter the height of the image: ")

# get the list of image files in the current directory
image_files = []
for file in os.listdir():
    if file.endswith(".jpg") or file.endswith(".png"):
        image_files.append(file)

# ask the user to select an image
for i, file in enumerate(image_files):
    print(f"{i}: {file}")

selected = input("Enter the number of the image you want to resize: ")
selected_file = image_files[int(selected)]

# open the selected image and resize it
img = Image.open(selected_file)
img = img.resize((int(width), int(height)))

# save the resized image
img.save(f"resized_{selected_file}")
