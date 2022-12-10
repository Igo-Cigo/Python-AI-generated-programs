# prompt used: make a cyrillic translator in python

# Define a dictionary of English to Cyrillic characters
english_to_cyrillic = {
    'a': 'а',
    'b': 'б',
    'c': 'ц',
    'd': 'д',
    'e': 'е',
    'f': 'ф',
    'g': 'г',
    'h': 'х',
    'i': 'и',
    'j': 'й',
    'k': 'к',
    'l': 'л',
    'm': 'м',
    'n': 'н',
    'o': 'о',
    'p': 'п',
    'q': 'к',
    'r': 'р',
    's': 'с',
    't': 'т',
    'u': 'у',
    'v': 'в',
    'w': 'ш',
    'x': 'х',
    'y': 'ы',
    'z': 'з'
}

# Define a function to translate a string of text
def translate_to_cyrillic(text):
    # Convert the text to lowercase
    text = text.lower()
    
    # Initialize an empty string to store the translated text
    translated_text = ""
    
    # Loop through each character in the text
    for char in text:
        # If the character is a letter, translate it to Cyrillic
        if char in english_to_cyrillic:
            translated_text += english_to_cyrillic[char]
        # Otherwise, leave it as is
        else:
            translated_text += char
    
    # Return the translated text
    return translated_text

# Prompt the user to enter a word
text = input("Enter a word to translate: ")

# Translate the word and print the result
print(translate_to_cyrillic(text))

