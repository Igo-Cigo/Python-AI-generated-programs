# English to Greek translator

# Define a dictionary of English to Greek characters
english_to_greek = {
    'a': 'α',
    'b': 'β',
    'c': 'ψ',
    'd': 'δ',
    'e': 'ε',
    'f': 'φ',
    'g': 'γ',
    'h': 'η',
    'i': 'ι',
    'j': 'υ',
    'k': 'κ',
    'l': 'λ',
    'm': 'μ',
    'n': 'ν',
    'o': 'ο',
    'p': 'π',
    'q': 'κ',
    'r': 'ρ',
    's': 'ς',
    't': 'τ',
    'u': 'θ',
    'v': 'υ',
    'w': 'ω',
    'x': 'χ',
    'y': 'υ',
    'z': 'ζ'
}

# Define a function to translate a string of text
def translate_to_greek(text):
    # Convert the text to lowercase
    text = text.lower()
    
    # Initialize an empty string to store the translated text
    translated_text = ""
    
    # Loop through each character in the text
    for char in text:
        # If the character is a letter, translate it to Greek
        if char in english_to_greek:
            translated_text += english_to_greek[char]
        # Otherwise, leave it as is
        else:
            translated_text += char
    
    # Return the translated text
    return translated_text

text = input("Enter a word to translate: ")
print(translate_to_greek(text))