"""
CAESAR CIPHER IMPLEMENTATION

The Caesar cipher is one of the simplest encryption techniques, named after
Julius Caesar who used it to protect military messages. Each letter in the
plaintext is shifted a certain number of positions down the alphabet.

For example, with a shift of 3:
- A becomes D
- B becomes E
- Z wraps around to C

This demonstrates:
- String manipulation and character iteration
- ASCII character codes (ord and chr functions)
- Modular arithmetic for wrapping (% operator)
- Algorithm implementation
- Encryption concepts for GCSE Computer Science

Note: This cipher is NOT secure for real-world use - it's purely educational!
"""
import datetime


def caesar_encrypt(text, shift):
    """
    Encrypt text using Caesar cipher with given shift value.
    Only encrypts letters, preserves spaces and punctuation.
    """
    result = ""
    
    for char in text:
        # Check if character is a letter
        if char.isalpha():
            # Get ASCII code
            ascii_code = ord(char)
            
            # Handle uppercase letters (A-Z are ASCII 65-90)
            if char.isupper():
                # Shift within uppercase range
                shifted = ((ascii_code - 65 + shift) % 26) + 65
            # Handle lowercase letters (a-z are ASCII 97-122)
            else:
                # Shift within lowercase range
                shifted = ((ascii_code - 97 + shift) % 26) + 97
            
            # Convert back to character and add to result
            result += chr(shifted)
        else:
            # Keep spaces, punctuation, numbers as-is
            result += char
    
    return result


def caesar_decrypt(text, shift):
    """
    Decrypt text by shifting in opposite direction.
    """
    # Decrypting is just encrypting with negative shift
    return caesar_encrypt(text, -shift)


def save_encrypted_message(original, encrypted, shift):
    """Save encrypted message to file"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("encrypted_messages.txt", "a") as file:
        file.write(f"\n{timestamp}\n")
        file.write(f"Original: {original}\n")
        file.write(f"Shift: {shift}\n")
        file.write(f"Encrypted: {encrypted}\n")
        file.write("-" * 50 + "\n")
    
    print("✓ Message saved to encrypted_messages.txt")


def display_menu():
    """Show main menu and get user choice"""
    print("\n" + "=" * 50)
    print("CAESAR CIPHER - ENCRYPTION & DECRYPTION")
    print("=" * 50)
    print("\n1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Brute force decrypt (try all shifts)")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        print("Please enter 1, 2, 3, or 4")


def get_shift_value():
    """Get valid shift value from user"""
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            print("Shift must be between 1 and 25")
        except ValueError:
            print("Please enter a number")


def encrypt_mode():
    """Interactive encryption mode"""
    print("\n--- ENCRYPT MODE ---")
    message = input("Enter message to encrypt: ")
    shift = get_shift_value()
    
    encrypted = caesar_encrypt(message, shift)
    
    print(f"\nOriginal message: {message}")
    print(f"Shift value: {shift}")
    print(f"Encrypted message: {encrypted}")
    
    # Save to file
    save_encrypted_message(message, encrypted, shift)


def decrypt_mode():
    """Interactive decryption mode"""
    print("\n--- DECRYPT MODE ---")
    message = input("Enter message to decrypt: ")
    shift = get_shift_value()
    
    decrypted = caesar_decrypt(message, shift)
    
    print(f"\nEncrypted message: {message}")
    print(f"Shift value: {shift}")
    print(f"Decrypted message: {decrypted}")


def brute_force_mode():
    """Try all possible shifts - useful when you don't know the shift value"""
    print("\n--- BRUTE FORCE DECRYPT ---")
    message = input("Enter encrypted message: ")
    
    print("\nTrying all possible shifts:\n")
    for shift in range(1, 26):
        decrypted = caesar_decrypt(message, shift)
        print(f"Shift {shift:2d}: {decrypted}")
    
    print("\nLook for the message that makes sense!")


# Main program
if __name__ == "__main__":
    print("Welcome to Caesar Cipher!")
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            encrypt_mode()
        elif choice == "2":
            decrypt_mode()
        elif choice == "3":
            brute_force_mode()
        elif choice == "4":
            print("\nGoodbye!")
            break