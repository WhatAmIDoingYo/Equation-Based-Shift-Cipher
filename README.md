# Equation-Based Shift Cipher


A fun, educational Python tool that turns text into long sequences of numbers using a custom mathematical equation as the secret key, plus an accumulating shift (delta).

Now fully cleaned up with a clean CLI, file I/O, and proper error handling.


## Features


- Single clean script (equation_shift_cipher.py)

- Full command-line interface (encrypt / decrypt)

- Supports direct messages, input files, and output files

- Fully customizable encryption equation (you control the math!)

- Adjustable shift increment (--delta)

- Robust error handling

- Zero external dependencies


## Installation

  

```bash

git  clone  https://github.com/WhatAmIDoingYo/Equation-Based-Shift-Cipher.git

cd  Equation-Based-Shift-Cipher

```

  

No extra packages needed — only uses Python’s standard library.

  

## Quick Start

  

### Encrypt

  

```bash

python  equation_shift_cipher.py  encrypt  "hello world"

```

  

**Example output:**

  
  

```text

Encrypted  message:  28062415317231793375374233863543

```

  

### Decrypt

  

```Bash

python  equation_shift_cipher.py  decrypt  28062415317231793375374233863543

```

  

**Example output:**

  



  

```text

Decrypted  message:  helloworld

```

  

> Note: Spaces, punctuation, and numbers are automatically removed.

  

## Full Usage

  

### Encrypt a message

  
  

```Bash

# Direct input

python  equation_shift_cipher.py  encrypt  "Your secret message"

  

# From file

python  equation_shift_cipher.py  encrypt  -i  input.txt  -o  encrypted.txt

  

# Custom delta

python  equation_shift_cipher.py  encrypt  "python is fun"  --delta  0.5

```

  

### Decrypt a message

  
  
  

```Bash

# Direct input

python  equation_shift_cipher.py  decrypt  28062415317231793375

  

# From file

python  equation_shift_cipher.py  decrypt  -i  encrypted.txt  -o  output.txt

```

  

## How It Works

  

1. Only alphabetic characters are kept (non-letters are removed).

2. Each letter becomes a number (a=1, b=2, …, z=26).

3. A small delta is added to each successive letter.

4. Your custom equation is applied → result is turned into 4-digit chunks.

5. Decryption reverses everything exactly.

  

## Customize the Math Key (The Cool Part!)

  

Edit these two functions in equation_shift_cipher.py:

  
  
  

```python

def  encrypt_equation(x: float) -> float:

"""Your encryption formula here"""

return (math.log10(x ** 2) + 1) * 1000

  

def  decrypt_equation(y: float) -> float:

"""Must be the exact mathematical inverse"""

return math.sqrt(10 ** ((y / 1000) - 1))

```

  

As long as decrypt_equation(encrypt_equation(x)) ≈ x, it works perfectly.

  

## Limitations

  

- Non-alphabetic characters (spaces, punctuation, etc.) are removed

- Output is always lowercase

- This is a mathematical/educational toy — not secure cryptography

- Use the exact same equation and delta for decryption

  

## Contributing

  

PRs welcome! Ideas for the future:

  

- Preset equations with auto-inverses

- Option to preserve spaces/punctuation

- Unit tests

- GUI version

  

## License

  

MIT License — see LICENSE for details.
