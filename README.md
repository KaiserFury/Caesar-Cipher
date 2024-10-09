# Caesar Cipher

## Description

This project is an implementation of the Caesar Cipher, a type of substitution cipher where each letter in the plaintext is shifted by a certain number of positions down or up the alphabet.

The Caesar Cipher is one of the simplest and most widely known encryption techniques. This implementation allows you to both encrypt and decrypt text using a shift value provided by the user.

## Features

- **Encryption**: Shifts the letters in the plaintext by a user-specified number of positions.
- **Decryption**: Reverts the shift, converting the ciphertext back to the original plaintext.
- Right now only supports lowercase letters.
- Retains non-alphabetic characters (e.g., numbers, punctuation) unchanged.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/KaiserFury/caesar-cipher.git
   cd caesar-cipher
   ```

2. Run the script:

   ```bash
   python caesar_cipher.py
   ```

3. Follow the prompts to either encrypt or decrypt text.

### Example

**Encryption:**

```
Type encode to 'encrypt,Type decode to 'decrypt': encode
Enter the your message (in lower case): hellow world
Enter the shift value: 3
Your encode message is : khoorz2zruog
```

**Decryption:**

```
Type encode to 'encrypt,Type decode to 'decrypt': decode
Enter the your message (in lower case): khoorz2zruog
Enter the shift number: 3
Your decode message is : hellow world
```

## How it Works

The Caesar Cipher works by shifting each letter in the input string by a specified number (shift value). For example, with a shift of 3:

- 'a' becomes 'd'
- 'b' becomes 'e'
- 'c' becomes 'f'

The shift wraps around the end of the alphabet, so 'z' with a shift of 1 becomes 'A'.

## Customization

You can easily modify the shift value to any number. Positive values shift to the right, while negative values shift to the left.

## Requirements

- Python 3.12


