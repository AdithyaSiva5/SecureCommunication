from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from polybius_cipher import polybius_encrypt, polybius_decrypt
from utils import sanitize_input

def main():
    print("Secure Communication Demo using Vigenere and Polybius Ciphers")

    message = input("Enter the message to encrypt: ")
    key = input("Enter the encryption key: ")

    # Sanitize input
    sanitized_message = sanitize_input(message)
    print(f"Sanitized message: {sanitized_message}")

    # Vigenere Encryption
    vigenere_encrypted = vigenere_encrypt(sanitized_message, key)
    print(f"\nVigenere Encrypted Text: {vigenere_encrypted}")

    # Polybius Encryption
    polybius_encrypted = polybius_encrypt(vigenere_encrypted)
    print(f"Polybius Encrypted Text: {polybius_encrypted}")

    # Decryption
    polybius_decrypted = polybius_decrypt(polybius_encrypted)
    print(f"Polybius Decrypted Text: {polybius_decrypted}")
    
    vigenere_decrypted = vigenere_decrypt(polybius_decrypted, key)
    print(f"\nFinal Decrypted Message: {vigenere_decrypted}")

    # Verify the decryption
    print(f"Original sanitized message: {sanitized_message}")
    print(f"Matches decrypted message: {sanitized_message == vigenere_decrypted}")

if __name__ == "__main__":
    main()