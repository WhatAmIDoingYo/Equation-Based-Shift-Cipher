# Equation-Based-Shift-Cipher

A Python-based encryption and decryption tool that transforms text messages into numerical sequences using a customizable, non-repeating equation as the encryption key and a dynamic shift (delta). This project includes two scripts: `Encrypt_v2.py` for encrypting text messages and `Decrypt_v2.py` for decrypting the resulting numerical sequences back to the original text.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Overview
Equation-Based-Shift-Cipher is a lightweight tool for encrypting and decrypting text messages. It uses a customizable equation (default: `y = (math.log10(x**2) + 1) * 1000`) as the encryption key to transform alphabetical characters into four-digit numerical codes, with an incremental shift (`delta = 0.1`) applied to each subsequent character for added complexity. The decryption process reverses this transformation to recover the original message.

The encryption equation can be any mathematical function, but it is strongly recommended to use a non-repeating (injective) function to ensure unique mappings for each input value, enhancing the security and reliability of the encryption.

- `Encrypt_v2.py`: Converts a text message into an encrypted numerical sequence using the specified equation.
- `Decrypt_v2.py`: Decrypts a numerical sequence back into the original text using the same equation.

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/WhatAmIDoingYo/Equation-Based-Shift-Cipher.git
   ```
3. Navigate to the repository directory:
   ```bash
   cd Equation-Based-Shift-Cipher
   ```
4. No additional dependencies are required as the scripts use only the standard `math` library.

## Usage
### Encryption
To encrypt a message, run `Encrypt_v2.py` with your desired message and equation defined in the script:
```bash
python Encrypt_v2.py
```
Modify the `message` variable and the `encrypt_number` function in `Encrypt_v2.py` to change the input text and encryption equation, respectively. The script outputs a numerical sequence.

### Decryption
To decrypt a numerical sequence, run `Decrypt_v2.py` with the encrypted message and the same equation used for encryption:
```bash
python Decrypt_v2.py
```
Modify the `encrypted_message` variable and the `decrypt_number` function in `Decrypt_v2.py` to change the input sequence and decryption equation. The script outputs the decrypted text.

**Note**: The encryption and decryption equations must match, and the decryption equation must be the exact inverse of the encryption equation for successful decryption. Using a non-repeating (injective) function is recommended to avoid ambiguous mappings.

## How It Works
- **Encryption**:
  1. Each alphabetical character is converted to a number (`a=1`, `b=2`, ..., `z=26`).
  2. A shift (`delta = 0.1`) is incrementally applied to each character's numerical value.
  3. The shifted value is transformed using the customizable encryption equation (default: `y = (math.log10(x**2) + 1) * 1000`) and formatted as a four-digit string.
  4. The result is a concatenated string of four-digit codes.

- **Decryption**:
  1. The input numerical sequence is split into four-digit chunks.
  2. Each chunk is reversed using the inverse of the encryption equation (default: `x = sqrt(10^((y/1000)-1))`).
  3. The incremental shift is subtracted to recover the original numerical value.
  4. The numerical value is converted back to a letter (`1=a`, `2=b`, ..., `26=z`).

- **Customizing the Equation**:
  The encryption equation serves as the key. You can modify the `encrypt_number` function in `Encrypt_v2.py` and the corresponding `decrypt_number` function in `Decrypt_v2.py` to use any mathematical function. For best results, choose a non-repeating (injective) function to ensure each input maps to a unique output. Ensure the decryption equation is the exact inverse of the encryption equation.

## Example
### Encryption
Input (`Encrypt_v2.py`):
```python
message = "hello"
delta = 0.1
def encrypt_number(x):
    y = (math.log10(x**2) + 1) * 1000
    return f"{int(y):04d}"
```
Output:
```text
Encrypted message: 30172448318434343708
```

### Decryption
Input (`Decrypt_v2.py`):
```python
encrypted_message = "30172448318434343708"
delta = 0.1
def decrypt_number(y, equation):
    if "math.log10" in equation:
        return math.sqrt(10 ** ((y / 1000) - 1))
    else:
        raise ValueError("Unsupported equation format")
```
Output:
```text
Decrypted message: hello
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or report bugs. Ensure your code follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines and includes clear comments.
