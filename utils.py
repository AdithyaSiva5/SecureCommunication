def sanitize_input(text):
    return ''.join(char.upper() for char in text if char.isalpha())