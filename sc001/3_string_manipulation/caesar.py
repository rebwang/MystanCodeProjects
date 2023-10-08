"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Decomposition:
    1. using secret number to create the new alphabet string
    2. case-insensitive
    3. find the deciphered string
    Create variables for each function in order to let functions pass-by-value!
    """
    secret_number = int(input('Secret number: '))  # Create a variable for the inputted secret number
    new = new_alphabet(secret_number)  # Find the new alphabet string
    string = input("What's the ciphered string? ")  # Create a variable for the inputted string
    ciphered_str = string.upper()  # Case insensitive: change the inputted string to upper cases
    ans = find_i(new, ciphered_str)  # Create a function to find the deciphered string
    print('The deciphered string is: ' + str(ans))


def new_alphabet(secret_number):
    """
    This function is to create the new alphabet string.
    Method: locate the defining index which separates the string into two parts by deducting secret number.
    """
    new = ''  # start with an empty string
    i = len(ALPHABET) - secret_number  # find the defining index
    new = ALPHABET[i:] + ALPHABET[:i]  # create new string by using reverse algorithm
    return new


def find_i(new, ciphered_str):
    """
    This function is to find the answer of deciphered string.
    """
    ans = ''  # Start with an empty string
    for i in range(len(ciphered_str)):  # Loop over the old string
        j = new.find(ciphered_str[i])  # using inputted string to locate the corresponding index in new alphabet string
        if j != -1:  # encounter non-alphabet object in the string
            ans += ALPHABET[j]  # retain whatever is there in the string
        else:
            ans += ciphered_str[i]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
