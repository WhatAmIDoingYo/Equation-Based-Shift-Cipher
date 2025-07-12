import math

# Encrypted message to be decrypted
encrypted_message = "372328161158361436192858249626523676218231582415301724483843343437083136371536403684281637302448325431213440297336762182389422252432352437743742344028793918355237953413324137713774343429642652327937922806323433043476348132602639388430663979364438653471361436603939338632733788279530823897282738723186312138813712375337193292364840423106361929553881388435003719392434653304373430343996407839153340307436843927309837713316358040263391321434023408379936103806404738463745405534503402364438333836404438093486397138844057400740103515341939913529405039993334371535054037392739003369384339964102339135933552340834133930357137743742344041523636397941593648406841193774407536683672378841573982364840933696366036234026400237533859411239853730369639363878397139744154"

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
