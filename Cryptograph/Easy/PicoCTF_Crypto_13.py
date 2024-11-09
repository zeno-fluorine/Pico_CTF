""" Pico CTF Challenge: 13
Author: Alex Fulton/Daniel Tunitis
Tags: Easy, Cryptography, picoCTF 2019

Description: Cryptography can be easy, do you know what ROT13 is?
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
"""

def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':  # lowercase letters
            # Shift character by 13 places and wrap around using modulo 26
            result.append(chr(((ord(char) - ord('a') + 13) % 26) + ord('a')))
        elif 'A' <= char <= 'Z':  # uppercase letters
            # Shift character by 13 places and wrap around using modulo 26
            result.append(chr(((ord(char) - ord('A') + 13) % 26) + ord('A')))
        else:
            result.append(char)  # non-alphabetical characters remain unchanged
    return ''.join(result)

# Example usage
encoded_text = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
decoded_text = rot13(encoded_text)
print("Decoded Text:", decoded_text)
