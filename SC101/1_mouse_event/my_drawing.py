"""
File: my_drawing.py
Name:
----------------------
This program draws a Baymax: head, face, upper body, lower body, right & left hands and legs.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Baymax is my favorite and the cutest character among all the animations!
    """
    window = GWindow()
    background = GRect(500, 500)
    background.filled = True
    background.fill_color = 'beige'
    window.add(background)
    head = GOval(100, 70)
    head.color = 'white'
    head.filled = True
    head.fill_color = 'white'
    window.add(head, x=window.width/2-head.width/2, y=window.height/10)

    l_eye = GOval(10, 10)
    l_eye.color = 'black'
    l_eye.filled = True
    l_eye.fill_color = 'black'
    window.add(l_eye, x=window.width/2-head.width/4, y=window.height/10+head.height/2)

    r_eye = GOval(10, 10)
    r_eye.color = 'black'
    r_eye.filled = True
    r_eye.fill_color = 'black'
    window.add(r_eye, x=window.width/2+head.width/8, y=window.height/10+head.height/2)

    mouth = GLine(l_eye.x, l_eye.y+l_eye.height/2, r_eye.x, r_eye.y+r_eye.height/2)
    window.add(mouth)

    upper_body = GOval(170, 170)
    upper_body.color = 'white'
    upper_body.filled = True
    upper_body.fill_color = 'white'
    window.add(upper_body, x=window.width/2-upper_body.width/2, y=window.height/5+head.height/8)

    lower_body = GOval(230, 210)
    lower_body.color = 'white'
    lower_body.filled = True
    lower_body.fill_color = 'white'
    window.add(lower_body, x=window.width/2-lower_body.width/2, y=window.height/3)

    l_leg = GOval(60, 100)
    l_leg.color = 'white'
    l_leg.filled = True
    l_leg.fill_color = 'white'
    window.add(l_leg, x=window.width/2-l_leg.width, y=window.height/2+lower_body.height/3)

    r_leg = GOval(60, 100)
    r_leg.color = 'white'
    r_leg.filled = True
    r_leg.fill_color = 'white'
    window.add(r_leg, x=window.width/2, y=window.height/2 + lower_body.height/3)

    l_hand = GOval(150, 50)
    l_hand.color = 'white'
    l_hand.filled = True
    l_hand.fill_color = 'white'
    window.add(l_hand, x=window.width/10, y=window.height/4)

    r_hand = GOval(150, 50)
    r_hand.color = 'white'
    r_hand.filled = True
    r_hand.fill_color = 'white'
    window.add(r_hand, x=window.width/2+window.width/10, y=window.height/4)

    name = GLabel("Hi, I am Baymax.", x=window.width/2+head.width/2, y=window.height/10)
    name.font = '-20'
    window.add(name)








if __name__ == '__main__':
    main()
