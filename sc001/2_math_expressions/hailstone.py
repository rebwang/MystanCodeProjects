"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Divide the given number by 2 to identify the number is even or odd. If remainder is 0 then it's even.
    """
    print('This program computes Hailstone sequences')
    n = int(input('Enter a number: '))
    step = 0
    while True:
        if n % 2 == 0:
            # When the given & new number is even
            print(str(n)+' is even, so I take half: '+str(n // 2))
            n = n // 2
            step += 1
        if n % 2 == 1:
            # When the given & new number is odd
            if n != 1:
                print(str(n)+' is odd, so I make 3n+1: '+str(3 * n + 1))
                n = 3 * n + 1
                step += 1
        if n == 1:
            break
    print('It took '+str(step)+' steps to reach 1.')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
