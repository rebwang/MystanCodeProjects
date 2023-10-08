"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    Create a function and use string manipulation to find the complement strand of DNA sequence.
    The function is able to replace the characters in old string with corresponding characters.
    Corresponding characters are as below:
    A - T
    C - G
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    if dna == '':  # When DNA is an empty string
        print('DNA strand is missing.', end="")
    ans = ""  # Start with an empty string
    for i in range(len(dna)):  # Loop over the old string
        ch = dna[i]
        if ch == 'A':
            ans += 'T'  # Concatenation
        if ch == 'T':
            ans += 'A'
        if ch == 'G':
            ans += 'C'
        if ch == 'C':
            ans += 'G'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
