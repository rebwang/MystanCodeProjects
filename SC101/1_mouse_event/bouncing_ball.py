"""
File: bouncing_ball.py
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(start)


def start(mouse):
    global count
    if ball.x == START_X or ball.y == START_Y:  # Only when ball is at START position will the click affect the program
        vy = 0
        while True:
            if count >= 3:
                break
            else:
                ball.move(VX, vy)
                vy += GRAVITY
                if ball.y >= window.height:
                    vy *= -REDUCE
                pause(DELAY)
                if ball.x >= window.width:
                    count += 1
                    break
        window.add(ball, x=START_X, y=START_Y)


if __name__ == "__main__":
    main()
