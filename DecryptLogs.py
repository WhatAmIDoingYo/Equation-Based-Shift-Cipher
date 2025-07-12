import math

# Encrypted message to be decrypted
encrypted_message = "23973764115832473429319324963273252635973602164428272598" 

# Increment value
delta = 0.1

# Define the encryption equation (for reference)
equation = "y = (math.log10(x**2) + 1) * 1000"

def decrypt_number(y, equation):
    # Reverse the encryption equation WITHOUT rounding
    if "math.log10" in equation:
        return math.sqrt(10 ** ((y / 1000) - 1))
    else:
        raise ValueError("Unsupported equation format")

def num_to_letter(num):
    return chr(int(num) + ord('a') - 1)

def decrypt_message(encrypted_message, delta, equation):
    decrypted_message = ''
    shift = 0
    for i in range(0, len(encrypted_message), 4):
        y = int(encrypted_message[i:i+4])
        raw_x = decrypt_number(y, equation)
        adjusted_x = raw_x - shift
        decrypted_message += num_to_letter(round(adjusted_x))
        shift += delta

    return decrypted_message

decrypted_message = decrypt_message(encrypted_message, delta, equation)
print(f"Decrypted message: {decrypted_message}")
