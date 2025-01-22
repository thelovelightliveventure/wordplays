"""Caesar cipher is a type of cipher that shifts each letter down by a certain number of letters.
This program encrypts and decrypts Caesar ciphers. """

def caesar_cipher(key, phrase, mode):
    """Function for encrypting or decrypting phrases."""
    result = []
    # Wrap key so letters stay within UNICODE limit
    shift = key % 26 if mode == "encrypt" else -key % 26

    # Encrypt/decrypt characters
    for char in phrase:
        if char.isalpha():
            if char.islower():
                letter = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if char.isupper():
                letter = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result.append(letter)
        else:
            result.append(char)

    return ("".join(result))

def encrypt(key, phrase):
    """Function for encrypting messages."""
    encrypted_phrase = caesar_cipher(key, phrase, "encrypt")
    print("-" * (len(encrypted_phrase) + 23))
    print(f"| Encrypted message: {encrypted_phrase} |")
    print("-" * (len(encrypted_phrase) + 23))
        

def decrypt(key, phrase):
    """Function for decrypting messages."""
    decrypted_phrase = caesar_cipher(key, phrase, "decrypt")
    print("-" * (len(decrypted_phrase) + 23))
    print(f"| Decrypted message: {decrypted_phrase} |")
    print("-" * (len(decrypted_phrase) + 23))

def main():
    """Main function"""
    try:    
        # Get user input
        key = int(input("Enter number of letters to shift by: "))
        phrase = input("Enter phrase to encrypt or decrypt: ").strip()
        action = input("Encrypt or decrypt (e/d)? ").strip().lower()
        
        # If phrase is empty
        if not phrase:
            print("No words entered. Please try again.")
            return

        # Find action and call corresponding function
        if action.startswith("e"):
            encrypt(key, phrase)
        elif action.startswith("d"):
            decrypt(key, phrase)
        else:
            print("Invalid type. Please try again.")
            return
        
    except ValueError:
        print("Please enter an integer as the key.")


if __name__ == "__main__":
    main()
