""" Pico CTF Challenge: interencdec
Author: NGIRIMANA Schadrack
Tags: Easy, Cryptography, picoCTF 2024, base64, browser_webshell_solvable, caesar

Description: Can you get the real meaning from this file.
Contents of the file: YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==
"""

import base64

# First base64 string to decode
base64_string_1 = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg=="
base64_bytes_1 = base64_string_1.encode("ascii")
sample_string_bytes_1 = base64.b64decode(base64_bytes_1)
decoded_string_1 = sample_string_bytes_1.decode("ascii")

# Output the first decoded string
print(f"Decoded string 1: {decoded_string_1}")

# Second base64 string to decode
base64_string_2 = "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=="
base64_bytes_2 = base64_string_2.encode("ascii")
sample_string_bytes_2 = base64.b64decode(base64_bytes_2)
decoded_string_2 = sample_string_bytes_2.decode("ascii")

# Output the second decoded string
print(f"Decoded string 2: {decoded_string_2}")

# Function to apply Caesar Cipher with a shift
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # only shift alphabetic characters
            # Shift uppercase letters
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Shift lowercase letters
            elif char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Non-alphabet characters remain the same
            result += char
    return result

# Function to display all shifts for a given string
def apply_all_shifts(decoded_string):
    for shift in range(1, 26):
        shifted_text = caesar_cipher(decoded_string, shift)
        print(f"Shift {shift}: {shifted_text}")


print("\nCaesar cipher shifts for decoded string 2:")
apply_all_shifts(decoded_string_2)

