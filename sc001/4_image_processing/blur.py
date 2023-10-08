"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    Create a blurred version of smiley-face image by creating blur(img) function.
    In the blur(img) function, if pixel (x, y), do the following steps:
    1. get pixels of all the adjacent neighbors
    2. get neighbor pixels' rgb
    3. new rgb of pixel(x, y) will be the avg of neighbor pixels' rgb
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img: str, the filepath of the original image
    :return: SimpleImage, the blurred version of the image
    """
    # Todo: create a new blank img that is as big as the original one
    old_img = SimpleImage("images/smiley-face.png")
    new_img = SimpleImage.blank(old_img.width, old_img.height)

    # Loop over the picture
    for x in range(new_img.width):
        for y in range(new_img.height):
            # Todo: get pixel of new_img at x,y
            pixel_b = new_img.get_pixel(x, y)

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            # Get pixel at the top-left corner of the image.
            if x == 0 and y == 0:
                a = old_img.get_pixel(x+1, y)
                b = old_img.get_pixel(x, y+1)
                c = old_img.get_pixel(x+1, y+1)
                pixel_b.red = (a.red+b.red+c.red) // 3
                pixel_b.green = (a.green+b.green+c.green) // 3
                pixel_b.blue = (a.blue+b.blue+c.blue) // 3

            # Get pixel at the top-right corner of the image.
            elif x == new_img.width-1 and y == 0:
                d = old_img.get_pixel(x-1, y)
                e = old_img.get_pixel(x, y+1)
                f = old_img.get_pixel(x-1, y+1)
                pixel_b.red = (d.red+e.red+f.red) // 3
                pixel_b.green = (d.green+e.green+f.green) // 3
                pixel_b.blue = (d.blue+e.blue+f.blue) // 3

            # Get pixel at the bottom-left corner of the image
            elif x == 0 and y == new_img.height-1:
                g = old_img.get_pixel(x, y-1)
                h = old_img.get_pixel(x+1, y)
                i = old_img.get_pixel(x+1, y-1)
                pixel_b.red = (g.red+h.red+i.red) // 3
                pixel_b.green = (g.green+h.green+i.green) // 3
                pixel_b.blue = (g.blue+h.blue+i.blue) // 3

            # Get pixel at the bottom-right corner of the image
            elif x == new_img.width-1 and y == new_img.height-1:
                j = old_img.get_pixel(x, y-1)
                k = old_img.get_pixel(x-1, y)
                l = old_img.get_pixel(x-1, y-1)
                pixel_b.red = (j.red + k.red + l.red) // 3
                pixel_b.green = (j.green + k.green + l.green) // 3
                pixel_b.blue = (j.blue + k.blue + l.blue) // 3

            # Get top edge's pixels (without two corners)
            elif x != 0 and x != new_img.width-1 and y == 0:
                m = old_img.get_pixel(x-1, y)
                n = old_img.get_pixel(x+1, y)
                o = old_img.get_pixel(x-1, y+1)
                p = old_img.get_pixel(x+1, y+1)
                q = old_img.get_pixel(x, y+1)
                pixel_b.red = (m.red + n.red + o.red + p.red + q.red) // 5
                pixel_b.green = (m.green + n.green + o.green + p.green + q.green) // 5
                pixel_b.blue = (m.blue + n.blue + o.blue + p.blue + q.blue) // 5

            # Get bottom edge's pixels (without two corners)
            elif x != 0 and new_img.width-1 and y == new_img.height-1:
                r = old_img.get_pixel(x-1, y)
                s = old_img.get_pixel(x+1, y)
                t = old_img.get_pixel(x-1, y-1)
                u = old_img.get_pixel(x+1, y-1)
                v = old_img.get_pixel(x, y-1)
                pixel_b.red = (r.red + s.red + t.red + u.red + v.red) // 5
                pixel_b.green = (r.green + s.green + t.green + u.green + v.green) // 5
                pixel_b.blue = (r.blue + s.blue + t.blue + u.blue + v.blue) // 5

            # Get left edge's pixels (without two corners)
            elif x == 0 and y != 0 and new_img.height-1:
                w = old_img.get_pixel(x, y-1)
                z = old_img.get_pixel(x, y+1)
                aa = old_img.get_pixel(x+1, y)
                bb = old_img.get_pixel(x+1, y+1)
                cc = old_img.get_pixel(x+1, y-1)
                pixel_b.red = (w.red + z.red + aa.red + bb.red + cc.red) // 5
                pixel_b.green = (w.green + z.green + aa.green + bb.green + cc.green) // 5
                pixel_b.blue = (w.blue + z.blue + aa.blue + bb.blue + cc.blue) // 5

            # Get right edge's pixels (without two corners)
            elif x == new_img.width-1 and y != 0 and new_img.height-1:
                dd = old_img.get_pixel(x, y-1)
                ee = old_img.get_pixel(x, y+1)
                ff = old_img.get_pixel(x-1, y+1)
                gg = old_img.get_pixel(x-1, y-1)
                hh = old_img.get_pixel(x-1, y)
                pixel_b.red = (dd.red + ee.red + ff.red + gg.red + hh.red) // 5
                pixel_b.green = (dd.green + ee.green + ff.green + gg.green + hh.green) // 5
                pixel_b.blue = (dd.blue + ee.blue + ff.blue + gg.blue + hh.blue) // 5

            # Inner pixels.
            else:
                ii = old_img.get_pixel(x-1, y-1)
                jj = old_img.get_pixel(x-1, y)
                kk = old_img.get_pixel(x-1, y+1)
                ll = old_img.get_pixel(x, y-1)
                mm = old_img.get_pixel(x, y+1)
                nn = old_img.get_pixel(x+1, y-1)
                oo = old_img.get_pixel(x+1, y)
                pp = old_img.get_pixel(x+1, y+1)
                pixel_b.red = (ii.red + jj.red + kk.red + ll.red + mm.red + nn.red + oo.red + pp.red) // 8
                pixel_b.green = (ii.green + jj.green + kk.green + ll.green + mm.green + nn.green + oo.green + pp.green) // 8
                pixel_b.blue = (ii.blue + jj.blue + kk.blue + ll.blue + mm.blue + nn.blue + oo.blue + pp.blue) // 8

    return new_img


if __name__ == '__main__':
    main()
