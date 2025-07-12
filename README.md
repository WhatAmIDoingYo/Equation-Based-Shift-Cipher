# Equation-Based-Shift-Cipher
Overview

Equation-Based-Shift-Cipher is a lightweight tool for encrypting and decrypting text messages. It uses a customizable equation (default: y = (math.log10(x**2) + 1) * 1000) as the encryption key to transform alphabetical characters into four-digit numerical codes, with an incremental shift (delta = 0.1) applied to each subsequent character for added complexity. The decryption process reverses this transformation to recover the original message.

The encryption equation can be any mathematical function, but it is strongly recommended to use a non-repeating (injective) function to ensure unique mappings for each input value, enhancing the security and reliability of the encryption.





Encrypt_v2.py: Converts a text message into an encrypted numerical sequence using the specified equation.



Decrypt_v2.py: Decrypts a numerical sequence back into the original text using the same equation.
