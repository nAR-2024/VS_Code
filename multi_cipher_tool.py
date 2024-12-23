def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift if mode == 'encrypt' else -shift
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    return result

def xor_cipher(text, key):
    return ''.join(chr(ord(char) ^ key) for char in text)

def apply_ciphers(text, mode='encrypt'):
    key = 3  # Example key for Caesar Cipher
    xor_key = 7  # Example key for XOR Cipher

    print("\nOriginal Text:", text)
    
    if mode == 'encrypt':
        caesar_result = caesar_cipher(text, key, mode)
        atbash_result = atbash_cipher(caesar_result)
        xor_result = xor_cipher(atbash_result, xor_key)
        print(f"Final Encrypted Text: {xor_result}")
        return xor_result
    elif mode == 'decrypt':
        xor_result = xor_cipher(text, xor_key)
        atbash_result = atbash_cipher(xor_result)
        caesar_result = caesar_cipher(atbash_result, key, mode)
        print(f"Final Decrypted Text: {caesar_result}")
        return caesar_result

def main():
    while True:
        print("\n--- Multi-Cipher Tool ---")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            apply_ciphers(text, mode='encrypt')
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            apply_ciphers(text, mode='decrypt')
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
