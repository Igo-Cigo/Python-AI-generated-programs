from PIL import Image, ImageDraw, ImageFont
import textwrap

# Ask the user for input
text = input('Enter some text: ')

# Create a new image with a white background
image = Image.new('RGB', (300, 300), color=(255, 255, 255))

# Wrap the text so that it fits on the image
wrapped_text = textwrap.wrap(text, width=25)

# Get the width and height of the text, so that we can center it on the image
text_width = max(len(line) for line in wrapped_text)
text_height = len(wrapped_text)

# Calculate the x and y coordinates to center the text
x = (300 - text_width * 10) / 2
y = (300 - text_height * 10) / 2

# Get a drawing context
draw = ImageDraw.Draw(image)

# Draw the text on the image
for line in wrapped_text:
    draw.text((x, y), line, fill=(0, 0, 0))
    y += 10

# Save the image
image.save('text_image.png')
