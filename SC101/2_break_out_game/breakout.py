"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 15         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    count = 0
    while True:
        graphics.collision()
        vx = graphics.get_dx()
        vy = graphics.get_dy()
        graphics.ball.move(vx, vy)
        pause(FRAME_RATE)
        if graphics.ball.y > graphics.window_height:
            count += 1
            if count == NUM_LIVES:
                label = GLabel('GAME OVER')
                graphics.window.add(label, x=graphics.window_width/2-label.width/2, y=graphics.window_height/2)
                break
            else:
                graphics.restart()


if __name__ == '__main__':
    main()
