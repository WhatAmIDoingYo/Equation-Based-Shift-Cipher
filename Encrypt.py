import math

# Message to be encrypted
message = "Example message"

# Increment value
delta = 0.1

def encrypt_number(x):
    # Equation used in the encryption
    y = (math.log10(x**2) + 1) * 1000
    return f"{int(y):04d}"

def letter_to_num(letter):
    return ord(letter.lower()) - ord('a') + 1

def encrypt_message(message, delta):
    encrypted_message = ''
    shift = 0

    for char in message:
        if char.isalpha():
            x = letter_to_num(char) + shift
            encrypted_message += encrypt_number(x)
            shift += delta

    return encrypted_message

encrypted_message = encrypt_message(message, delta)
print(f"Encrypted message: {encrypted_message}")

