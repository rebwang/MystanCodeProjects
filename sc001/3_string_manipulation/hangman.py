"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Create variables for N_TURNS(constant), random word, and dashed version of word.
    These variables will be used in the guess function (pass by value)
    """
    count = N_TURNS
    word = random_word()
    ans = start(word)
    print('THe word looks like ' + str(ans))
    print('You have 7 guesses left.')
    guess(word, ans, count)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def start(word):
    """
    This function will replace the word with dash.
    """
    ans = ""
    for i in range(len(word)):
        ans += '-'
    return ans


def guess(word, ans, count):
    """
    This function set the rules of the game:
    1. only N_TURNS wrong guesses allowed
    2. No illegal format: non-alpha or more than one character
    3. case insensitive
    4. identify wrong guess or right guess
    """
    while True:
        if count == 0:  # running out of wrong guess quota, game over
            print('You are completely hung : (')
            print('The word was: ' + str(word))
            break
        input_ch = str(input('Your guess: '))
        if len(input_ch) > 1:  # user type in more than one character
            print('Illegal format.')
        elif input_ch.isalpha() == False:  # user's input is non-alpha
            print('Illegal format.')
        else:
            input_1 = input_ch.upper()  # case insensitive
            if word.find(input_1) == -1:  # user's input does not match with the answer
                count -= 1
                wrong_guess(count, ans, input_1)
            else:
                new_ans = right_guess(ans, input_1, word, count)  # user's input matches with the answer
                ans = new_ans
                if new_ans.isalpha() == True:  # identify whether all the characters are correctly guessed and revealed
                    break  # user win, game over


def wrong_guess(count, ans, input_1):
    """
    This function will run if user's input doesn't match with the answer, and deduct wrong guess quota for each time.
    """
    if count != 0:
        print('There is no ' + str(input_1) + "'s in the word.")
        print('The word looks like ' + str(ans))
        print('You have ' + str(count) + ' wrong guesses left.')


def right_guess(ans, input_1, word, count):
    """
    This function will run if user's input matched with the answer.
    This function will replace the dash with user's input at the corresponding index, and update the variable with new string.
    """
    new_ans = ""
    for i in range(len(word)):
        ch = word[i]
        ch_1 = ans[i]
        if ch_1.isalpha() == True:  # retain right guesses from the previous rounds
            new_ans += ch_1
        else:
            if ch == input_1:  # replace dash with the correct user input
                new_ans += ch
            else:
                new_ans += "-"  # characters that are yet to be revealed
    print('You are correct!')
    if new_ans.isalpha() == True:  # identify whether all the characters are correctly guessed and revealed
        print('You win!!')
        print('The word was: ' + str(word))
    else:
        print('The word looks like ' + str(new_ans))
        print('You have ' + str(count) + ' wrong guesses left.')
    return new_ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
