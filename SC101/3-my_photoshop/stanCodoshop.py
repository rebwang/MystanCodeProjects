"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    r = (red - pixel.red)**2
    g = (green - pixel.green)**2
    b = (blue - pixel.blue)**2
    color_distance = math.sqrt(r+g+b)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    r_total = 0
    g_total = 0
    b_total = 0
    lst = []
    for i in range(len(pixels)):
        ele = pixels[i]
        r_total += ele.red
        g_total += ele.green
        b_total += ele.blue
    r_avg = r_total//len(pixels)
    g_avg = g_total//len(pixels)
    b_avg = b_total//len(pixels)
    lst.append(r_avg)
    lst.append(g_avg)
    lst.append(b_avg)
    return lst


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_point = get_average(pixels)
    red = avg_point[0]
    green = avg_point[1]
    blue = avg_point[2]
    d = {}
    for i in range(len(pixels)):
        pixel = pixels[i]
        dist = get_pixel_dist(pixel, red, green, blue)
        d[pixel] = dist
    best = min(d, key=d.get)
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for y in range(result.height):
        for x in range(result.width):
            pixels = []  # 放這裡是因為要清空list存下一顆三張照片裡的pixel
            for k in range(len(images)):
                img = images[k]
                pixel = img.get_pixel(x, y)
                pixels += [pixel]
            final_pixel = get_best_pixel(pixels)
            new_pixel = result.get_pixel(x, y)
            new_pixel.red = final_pixel.red
            new_pixel.green = final_pixel.green
            new_pixel.blue = final_pixel.blue
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
