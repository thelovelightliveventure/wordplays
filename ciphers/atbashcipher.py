"""The Atbash cipher, also called the reverse alphabet or backwards cipher, is a type of substitution
cipher originally used for the Hebrew alphabet. This program encrypts and decrypts messages by the Atbash
cipher."""

def atbash_cipher(message):
    """Function for setting up encryption and decryption of messages."""
    result = []

    # Encrypt/decrypt characters
    for char in message:
        if char.isalpha():
            if char.islower():
                letter = chr(ord("a") + ord("z") - ord(char))
            elif char.isupper():
                letter = chr(ord("A") + ord("Z") - ord(char))
            result.append(letter)
        else:
            result.append(char)

    return("".join(result))


def main():
    """Main function."""
    
    # Welcome user to program
    print("Welcome to the Atbash Cipher Program!")
    print("This program will encrypt or decrypt your message using the Atbash cipher.")
    print("#" * 40)

    # Get user input
    message = input("Enter message here: ").strip()
    mode = input("Mode: encrypt or decrypt (e/d)? ")

    if not message:
        print("No words entered. Please try again.")
        return
    
    result = atbash_cipher(message)

    # Print result
    print("#" * 40)
    if mode.startswith("e"):
        print(f"Encrypted message: {result}")
    elif mode.startswith("d"):
        print(f"Decrypted message: {result}")
    else:
        print("Invalid mode. Please try again.")
        return
    print("#" * 40)

if __name__ == "__main__":
    main()
