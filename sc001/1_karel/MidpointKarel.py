"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel's mission is to find midpoint in all worlds in different sizes.
    At first, Karel will move to the upper left of the world.
    Then move by following the pattern: East, South, South repetitively until reaching 1st street.
    When reaching 1st Street, Karel will be on the midpoint and put one beeper to complete the mission.
    """
    turn_left()
    while front_is_clear():
        move()
    turn_right()
    while facing_east():
        if front_is_clear():
            move()
            turn_right()
        if front_is_clear():
            move()
        if front_is_clear():
            move()
        if front_is_clear():
            turn_left()
    if not front_is_clear():
        put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
