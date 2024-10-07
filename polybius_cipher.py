POLYBIUS_SQUARE = {
    'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
    'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '25',
    'K': '31', 'L': '32', 'M': '33', 'N': '34', 'O': '35',
    'P': '41', 'Q': '42', 'R': '43', 'S': '44', 'T': '45',
    'U': '51', 'V': '52', 'W': '53', 'X': '54', 'Y': '55', 'Z': '00'
}

def polybius_encrypt(plaintext):
    return ' '.join(POLYBIUS_SQUARE[char] for char in plaintext)

def polybius_decrypt(ciphertext):
    reverse_square = {v: k for k, v in POLYBIUS_SQUARE.items()}
    return ''.join(reverse_square[pair] for pair in ciphertext.split())