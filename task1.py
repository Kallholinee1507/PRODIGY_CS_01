def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# User Input
choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").strip().upper()
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g. 3): "))

if choice == 'E':
    encrypted = caesar_encrypt(message, shift)
    print("Encrypted message:", encrypted)
elif choice == 'D':
    decrypted = caesar_decrypt(message, shift)
    print("Decrypted message:", decrypted)
else:
    print("Invalid choice. Please select E or D.")
