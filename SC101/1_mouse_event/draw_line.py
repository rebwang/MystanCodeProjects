"""
File: draw_line.py
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
window = GWindow()
first_click = True  # A switch to identify first click or second click
circle = GOval(SIZE*2, SIZE*2)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    global first_click
    if first_click:
        window.add(circle, x=event.x-SIZE, y=event.y-SIZE)
        first_click = False
    else:
        line = GLine(circle.x, circle.y, event.x, event.y)
        window.add(line)
        window.remove(circle)
        first_click = True


if __name__ == "__main__":
    main()
