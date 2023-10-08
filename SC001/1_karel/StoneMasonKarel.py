"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    In this world, Karel will fill up pillars till the last avenue.
    Initial position: Karel is at (1, 1) facing East.
    End position: Karel is on the last avenue, 1st Street, facing east.
    Condition: Each pillar is 5 beepers tall, 4 avenues away.
    """
    while front_is_clear():
        fill_pillar()
        go_back()
        move_to_next_pillar()
    fill_pillar()
    go_back()
    turn_left()


def fill_pillar():
    """
    Pre-condition: Karel at street 1, facing East
    Post-condition: Karel at street 5, facing North
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()


def go_back():
    """
    Pre-condition: Karel is at street 5, facing North
    Post-condition: Karel is at street 1, facing South
    """
    if not on_beeper():
        put_beeper()
    turn_around()
    for i in range(4):
        move()


def turn_around():
    turn_left()
    turn_left()


def move_to_next_pillar():
    """
    Pre-condition: Karel is at street 1, facing South
    Post-condition: Karel is at the next pillar street 1, facing East
    """
    turn_left()
    for i in range(4):
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
