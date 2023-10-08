"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 6


def main():
    """
    The rocket is composed by 6 small parts: head, belt, upper, lower, belt, head.
    Create functions for head, belt, upper and lower.
    Use at least one for loop in each function, and use constant and index to define loop patterns.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end="")
        for j in range(i+1):
            print('/', end="")
        for j in range(i+1):
            print('\\', end="")
        for j in range(SIZE-i):
            print(' ', end="")
        print("")


def belt():
    print('+', end="")
    for i in range(1):
        for j in range(SIZE * 2):
            print('=', end="")
    print('+', end="")
    print("")


def upper():
    for i in range(SIZE):
        print('|', end="")
        for j in range(SIZE-1-i):
            print('.', end="")
        for j in range(i+1):
            print('/\\', end="")
        for j in range(SIZE-1-i):
            print('.', end="")
        print('|', end="")
        print("")


def lower():
    for i in range(SIZE):
        print('|', end="")
        for j in range(i):
            print('.', end="")
        for j in range(SIZE-i):
            print('\\/', end="")
        for j in range(i):
            print('.', end="")
        print('|', end="")
        print("")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
