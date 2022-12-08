from PIL import Image, ImageDraw, ImageFont

# List of available fonts
fonts = ['arial.ttf', 'times.ttf', 'courier.ttf', 'helvetica.ttf']

# Print the available fonts and their numbers
    
# Text to be converted to image
text = input("Enter the text to convert to an image: ")

for i, font in enumerate(fonts):
    print(f"{i+1}: {font}")

# Prompt the user to select a font by its number
selected_font = fonts[int(input("Select a font by its number: ")) - 1]

# Get the lenght of text
text_lenght = len(text)*21

# Create a new image
img = Image.new('RGB', (text_lenght, 50), color = (73, 109, 137))

# Create a new drawing context
draw = ImageDraw.Draw(img)

# Use the selected font to write the text on the image
font = ImageFont.truetype(selected_font, 24)
draw.text((10, 10), text, font=font, fill=(255, 255, 0))

# Save the image to a file
img.save('text_image.png')
