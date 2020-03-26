'''
1. Design a web portal to upload the image files.
2.Implement at least three out the following 6 image filtering functions: Gray, Sepia, Poster, Blur, Edge, and Solar.
3.Store the images in AWS S3 storage
4.Display the processed image
5.A web portal to download the processed image
'''

from PIL import Image, ImageFilter
import sys

# Gray
def gray(image):
    return image.convert('L')

# Sepia
def sepia(image):
    width, height = image.size
    new_img = image.copy()

    for x in range(width):
        for y in range(height):
            red, green, blue = image.getpixel((x, y))
            new_val = (0.3 * red + 0.59 * green + 0.11 * blue)

            new_red = int(new_val * 2)
            if new_red > 255:
                new_red = 255
            new_green = int(new_val * 1.5)
            if new_green > 255:
                new_green = 255
            new_blue = int(new_val)
            if new_blue > 255:
                new_blue = 255

            new_img.putpixel((x, y), (new_red, new_green, new_blue))

    return new_img

# Poster
def poster(image):
    return ""

# Blur
def blur(image):
    return image.filter(ImageFilter.GaussianBlur(radius=3))

# Edge
def edge(image):
    return image.filter(ImageFilter.EDGE_ENHANCE_MORE)

# Solar
def solar(image):
    return ""

# Image reading and manipulation
# try:
#     img = Image.open("C:\\Users\\Allison Aprile\\Pictures\\Doggies\\Owen\\Owie.jpg")
#
# except IOError:
#     print("Unable to load image")
#     sys.exit(1)
#
# i = sepia(img)
# i.show()