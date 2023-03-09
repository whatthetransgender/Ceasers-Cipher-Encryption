def shift_text(text, shift):

    result = ""

    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift

            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26

            result += chr(shifted)
        else:
            result += char

    return result


def encrypt(text, shift):

    return shift_text(text, shift)


def decrypt(text, shift):
    return shift_text(text, -shift)

text = input("Enter text to process: ")

while True:
    try:
        shift = int(input("Enter shift amount: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

while True:
    mode = input("Encrypt or decrypt? [e/d]: ").lower()
    if mode == 'e':

        processed_text = encrypt(text, shift)
        print("Encrypted text:", processed_text)
        break
    elif mode == 'd':

        processed_text = decrypt(text, shift)
        print("Decrypted text:", processed_text)
        break
    else:
        print("Invalid input. Please enter 'e' to encrypt or 'd' to decrypt.")
