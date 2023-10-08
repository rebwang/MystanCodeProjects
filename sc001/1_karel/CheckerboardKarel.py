"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    In this world, Karel will draw a checkerboard by using beeper to represent checkered pattern.
    Meaning wherever a beeper is, the adjacent street and avenue should not have a beeper regardless of directions.
    Pre-condition: Karel is at (1, 1), facing East. Karel will start with putting a beeper at (1, 1).
    Karel will draw the checkerboard from bottom(South) to top(North).
    Start with moving East in the first row, and moving West in the next.
    """
    put_beeper()
    if front_is_clear():
        fill_one_line_east()
        while front_is_clear():
            if left_is_clear():
                fill_one_line_west()
            if right_is_clear():
                fill_one_line_east()
    else:
        turn_left()
        # Karel is facing North
        fill_one_line_north()
        while front_is_clear():
            if right_is_clear():
                fill_one_line_south()
            if left_is_clear():
                fill_one_line_north()


def fill_one_line_east():
    while facing_east():
        if front_is_clear():
            # to determine if Karel reach the East wall
            if on_beeper():
                # to determine whether next step should put a beeper
                move()
            else:
                move()
                put_beeper()
        else:
            # Karel reach the East wall
            turn_left()
            if front_is_clear():
                # to determine if Karel reach the North wall
                if on_beeper():
                    move()
                    turn_left()
                else:
                    move()
                    put_beeper()
                    turn_left()


def fill_one_line_west():
    while facing_west():
        if front_is_clear():
            if on_beeper():
                move()
            else:
                move()
                put_beeper()
        else:
            turn_right()
            if front_is_clear():
                if on_beeper():
                    move()
                    turn_right()
                else:
                    move()
                    put_beeper()
                    turn_right()


def fill_one_line_north():
    while facing_north():
        if front_is_clear():
            if on_beeper():
                move()
            else:
                move()
                put_beeper()
        else:
            turn_right()
            if front_is_clear():
                if on_beeper():
                    move()
                    turn_right()
                else:
                    move()
                    put_beeper()
                    turn_right()


def fill_one_line_south():
    while facing_south():
        if front_is_clear():
            if on_beeper():
                move()
            else:
                move()
                put_beeper()
        else:
            turn_left()
            if front_is_clear():
                if on_beeper():
                    move()
                    turn_left()
                else:
                    move()
                    put_beeper()
                    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


#     put_beeper()
#     fill_one_line_east()
#     while front_is_clear():
#         if left_is_clear():
#             fill_one_line_west()
#         if right_is_clear():
#             fill_one_line_east()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
