import argparse
import math
import sys
from typing import Optional

def letter_to_num(letter: str) -> int:
    """Convert a-z/A-Z to 1-26."""
    return ord(letter.lower()) - ord('a') + 1

def num_to_letter(num: float) -> str:
    """Convert rounded number back to a-z (lowercase)."""
    return chr(int(round(num)) + ord('a') - 1)

# ==================== CUSTOMIZE HERE ====================
# Change these two functions to use a different equation.
# They MUST be mathematical inverses of each other!
def encrypt_equation(x: float) -> float:
    """Default: y = (log10(x²) + 1) * 1000"""
    return (math.log10(x ** 2) + 1) * 1000

def decrypt_equation(y: float) -> float:
    """Inverse of the default equation."""
    return math.sqrt(10 ** ((y / 1000) - 1))
# =======================================================

def encrypt_message(message: str, delta: float = 0.1) -> str:
    """Encrypt only alphabetic characters (non-letters are removed)."""
    encrypted = ''
    shift = 0.0
    for char in message:
        if char.isalpha():
            x = letter_to_num(char) + shift
            y = encrypt_equation(x)
            encrypted += f"{int(y):04d}"
            shift += delta
    return encrypted

def decrypt_message(encrypted_message: str, delta: float = 0.1) -> str:
    """Decrypt pure 4-digit string back to text."""
    if len(encrypted_message) % 4 != 0:
        raise ValueError("Encrypted message length must be a multiple of 4")
    decrypted = ''
    shift = 0.0
    for i in range(0, len(encrypted_message), 4):
        chunk = encrypted_message[i:i+4]
        if not chunk.isdigit():
            raise ValueError(f"Invalid chunk (not 4 digits): {chunk}")
        y = int(chunk)
        raw_x = decrypt_equation(y)
        adjusted_x = raw_x - shift
        decrypted += num_to_letter(adjusted_x)
        shift += delta
    return decrypted

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Equation-Based Shift Cipher - CLI tool with customizable math key"
    )
    subparsers = parser.add_subparsers(dest="mode", required=True)

    # Encrypt subcommand
    enc = subparsers.add_parser("encrypt", help="Encrypt a message")
    enc.add_argument("message", nargs="?", help="Message to encrypt")
    enc.add_argument("-i", "--input-file", help="Read message from file")
    enc.add_argument("-o", "--output-file", help="Write encrypted output to file")
    enc.add_argument("--delta", type=float, default=0.1, help="Shift increment (default 0.1)")

    # Decrypt subcommand
    dec = subparsers.add_parser("decrypt", help="Decrypt an encrypted string")
    dec.add_argument("encrypted", nargs="?", help="Encrypted digit string")
    dec.add_argument("-i", "--input-file", help="Read encrypted string from file")
    dec.add_argument("-o", "--output-file", help="Write decrypted text to file")
    dec.add_argument("--delta", type=float, default=0.1, help="Shift increment (default 0.1)")

    args = parser.parse_args()

    if args.mode == "encrypt":
        # Get input
        if args.input_file:
            with open(args.input_file, "r", encoding="utf-8") as f:
                msg = f.read()
        elif args.message:
            msg = args.message
        else:
            msg = input("Enter message to encrypt: ")

        result = encrypt_message(msg, args.delta)
        if args.output_file:
            with open(args.output_file, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Encrypted to {args.output_file}")
        else:
            print("Encrypted message:", result)

    elif args.mode == "decrypt":
        # Get input
        if args.input_file:
            with open(args.input_file, "r", encoding="utf-8") as f:
                enc_str = f.read().strip()
        elif args.encrypted:
            enc_str = args.encrypted
        else:
            enc_str = input("Enter encrypted string: ")

        try:
            result = decrypt_message(enc_str, args.delta)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

        if args.output_file:
            with open(args.output_file, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Decrypted to {args.output_file}")
        else:
            print("Decrypted message:", result)

if __name__ == "__main__":
    main()