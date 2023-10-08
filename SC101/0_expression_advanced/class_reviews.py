"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
# The constant controls when to stop calculating scores and exit
EXIT = -1  # data type: int


def main():
    """
    User will enter a class name, either SC001 or SC101 (data type: str), and then enter a score (data type: int).
    Each score entered will be compared with the previous max and min score.
    At the end of this program, the max, min and avg for each class will be calculated and printed.
    """
    count_001 = 0
    count_101 = 0

    # First input
    c = input('Which class? ')
    if c == str(EXIT):  # If user input == constant
        print('No class scores were entered')
    else:
        c1 = c.upper()  # Case insensitive
        score = int(input('Score: '))
        if c1 == 'SC001':
            max_001 = score
            min_001 = score
            total_001 = score
            count_001 += 1
        else:
            max_101 = score
            min_101 = score
            total_101 = score
            count_101 += 1

        # The rest of the inputs
        while True:
            c = input('Which class? ')
            if c == str(EXIT):
                break
            else:
                c1 = c.upper()
                score = int(input('Score: '))
                if c1 == 'SC001':
                    if count_001 == 0:  # use count to identify whether 1st record exists
                        max_001 = score
                        min_001 = score
                        total_001 = score
                        count_001 += 1
                    else:
                        if score > max_001:
                            max_001 = score
                        if score < min_001:
                            min_001 = score
                        total_001 += score
                        count_001 += 1
                else:
                    if count_101 == 0:
                        max_101 = score
                        min_101 = score
                        total_101 = score
                        count_101 += 1
                    else:
                        if score > max_101:
                            max_101 = score
                        elif score < min_101:
                            min_101 = score
                        total_101 += score
                        count_101 += 1

        print('=============SC001=============')

        if count_001 == 0:
            print('No score for SC001')
        else:
            print('Max (001): ' + str(max_001))
            print('Min (001): ' + str(min_001))
            print('Avg (001): ' + str(total_001 / count_001))

        print('=============SC101=============')

        if count_101 == 0:
            print('No score for SC101')
        else:
            print('Max (101): ' + str(max_101))
            print('Min (101): ' + str(min_101))
            print('Avg (101): ' + str(total_101 / count_101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
