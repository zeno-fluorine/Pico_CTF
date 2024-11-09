""" Pico CTF Challenge: interencdec
Author: DANNY
Tags: East, Cryptography, picoCTF 2019

Description: The Numbers... what do they mean?
Links to a picture with the following numbers: 16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14
"""


def numbers_to_letters(num_str):
    # Create an empty string to hold the result
    result = ""
    
    # Split the input string by commas and iterate over each number
    for num in num_str.split(','):
        if num.isdigit():  # Check if the value is a digit
            # Convert the number to an integer and get the corresponding letter (1 -> A, 2 -> B, etc.)
            letter = chr(int(num) + ord('A') - 1)
            result += letter
        else:
            raise ValueError("Input must be a string of comma-separated digits.")
    
    return result

# Example usage:
num_str = "16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14"
try:
    letters = numbers_to_letters(num_str)
    print(f"The corresponding letters are: {letters}")
except ValueError as e:
    print(e)
