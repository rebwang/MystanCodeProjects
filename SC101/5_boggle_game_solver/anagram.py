"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dic = []
anagrams = []
counter = 0


def main():
    """
    Use recursion to find meaningful anagrams from dictionary of a given string
    """
    print('Welcome to StanCode "Anagram Generator" (or -1 to quit)')
    global anagrams, counter
    read_dictionary()
    while True:
        lookup = input('Find anagrams for: ')
        start = time.time()
        if lookup == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(lookup)
            print(str(counter), 'anagrams:', anagrams)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')

            # refresh counter and anagram list before next user input
            counter = 0
            anagrams = []


def read_dictionary():
    global dic
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            dic += word.split()


def find_anagrams(s):
    """
    :param s: string, user's input, the word to lookup for
    :return: list, a list of anagrams
    """
    find_anagrams_helper(s, "")


def find_anagrams_helper(s, current_s):
    global anagrams, counter
    if len(s) == 0:  # base case
        if current_s in dic and current_s not in anagrams:
            anagrams.append(current_s)
            counter += 1
            print(f'Found: {current_s}')
            print('Searching...')
    else:
        for i in range(len(s)):
            if has_prefix(current_s):  # to check if the prefix exists in dictionary
                # choose
                current_s += s[i]
                # explore
                new_s = s[:i]+s[i+1:]  # subtract s[i] from old s to avoid repetitive characters
                find_anagrams_helper(new_s, current_s)  # use new s to run recursion
                # un-choose
                current_s = current_s[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: current_s in function find_anagrams_helper()
    :return: Whether there are words start with sub_s, return True or False
    """
    for word in dic:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
