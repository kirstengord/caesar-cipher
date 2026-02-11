# Caesar Cipher Encoder/Decoder

A Python implementation of the Caesar cipher - one of the simplest encryption techniques, named after Julius Caesar. This educational project demonstrates classical cryptography concepts for GCSE Computer Science students.

## Features
- Encrypt messages with custom shift values (1-25)
- Decrypt messages when you know the shift value
- Brute force mode - try all 25 possible shifts to crack unknown encryptions
- Saves encrypted messages with timestamps to a file
- Preserves spaces, punctuation, and capitalization

## Concepts Demonstrated
- String manipulation and character iteration
- ASCII character codes (`ord()` and `chr()` functions)
- Modular arithmetic for alphabet wrapping (`%` operator)
- Algorithm implementation
- Input validation and error handling
- File handling for persistent storage

## How It Works

The Caesar cipher shifts each letter by a fixed number of positions in the alphabet:
- With shift 3: A→D, B→E, Z→C (wraps around)
- Example: "HELLO" with shift 3 becomes "KHOOR"

The algorithm uses ASCII codes and modular arithmetic to handle wrapping:
```python
shifted = ((ascii_code - 65 + shift) % 26) + 65
```

## How to Run

**Prerequisites:**
- Python 3.14 installed on your system

**Steps:**
1. Download `caesar_cipher.py` from this repository
2. Open terminal/command prompt
3. Navigate to the download folder
4. Run: `python caesar_cipher.py`
5. Follow the on-screen menu

**Alternative - Clone the repository:**
```bash
git clone https://github.com/kirstengord/caesar-cipher.git
cd caesar-cipher
python caesar_cipher.py
```

## Example Usage
```
==================================================
CAESAR CIPHER - ENCRYPTION & DECRYPTION
==================================================

1. Encrypt a message
2. Decrypt a message
3. Brute force decrypt (try all shifts)
4. Exit

Enter your choice (1-4): 1

--- ENCRYPT MODE ---
Enter message to encrypt: Hello World
Enter shift value (1-25): 3

Original message: Hello World
Shift value: 3
Encrypted message: Khoor Zruog
✓ Message saved to encrypted_messages.txt
```

## Educational Context

This project was created to demonstrate understanding of:
- Fundamental programming concepts (loops, conditionals, functions)
- String processing algorithms
- Basic cryptography principles
- Real-world applications of modular arithmetic

**Note:** The Caesar cipher is not secure for real-world use - it can be easily broken with brute force or frequency analysis. This is purely an educational implementation.

## Future Enhancements
- Add frequency analysis to auto-detect most likely shift
- Support for additional character sets
- GUI interface
- Export encrypted messages in different formats
