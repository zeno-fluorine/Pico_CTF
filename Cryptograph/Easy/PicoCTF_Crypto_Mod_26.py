""" Pico CTF Challenge: MOD 26
Author: PANDU
Tags: Easy, Cryptography, picoCTF 2021

Description: Cryptography can be easy, do you know what ROT13 is? 
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}
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
encoded_text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"
decoded_text = rot13(encoded_text)
print("Decoded Text:", decoded_text)
