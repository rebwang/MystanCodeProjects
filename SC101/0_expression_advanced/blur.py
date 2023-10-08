"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the original img
    :return: the blurred version of original img
    """
    old_img = SimpleImage('images/smiley-face.png')
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    for y in range(old_img.height):
        for x in range(old_img.width):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < old_img.width:  # 上限不包含
                        if 0 <= pixel_y < old_img.height:  # 上限不包含
                            pixel = old_img.get_pixel(pixel_x, pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = r_sum / count
            new_pixel.green = g_sum / count
            new_pixel.blue = b_sum / count
    return new_img


def main():
    """
    Create a blur function to calculate and get the new pixel RBG from the original img.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
