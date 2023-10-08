"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Initial position: Karel is at (4, 3) facing East, beeper is at (3, 6).
    In this world, Karel will go out and pick up beeper, return back to initial position, then put down beeper.
    """
    go_out()
    pick_beeper()
    turn_around()
    go_back()
    put_beeper()


def go_out():
    """
    Pre-condition: Karel is at (4, 3) facing East
    Post-condition: Karel is at (3. 6) facing East
    """
    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


def go_back():
    """
    Pre-condition: Karel is at (3, 6) facing West
    Post-condition: Karel is at (4, 3) facing East
    """
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
