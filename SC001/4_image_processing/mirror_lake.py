"""
File: mirror_lake.py
Name:
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return: SimpleImage, mirrored version of image
    """
    img = SimpleImage('images/mt-rainier.jpg')
    b_img = SimpleImage.blank(img.width, img.height*2)
    b_img.show()

    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            b_img_pixel1 = b_img.get_pixel(x, y)
            b_img_pixel1.red = img_pixel.red
            b_img_pixel1.green = img_pixel.green
            b_img_pixel1.blue = img_pixel.blue

            b_img_pixel2 = b_img.get_pixel(x, b_img.height-1-y)
            b_img_pixel2.red = img_pixel.red
            b_img_pixel2.green = img_pixel.green
            b_img_pixel2.blue = img_pixel.blue
    return b_img


def main():
    """
    Create a mirrored version of original image by creating reflect() function
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
