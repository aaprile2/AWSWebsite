from PIL import Image, ImageOps, ImageFilter
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
    return ImageOps.posterize(image, 3)

# Blur
def blur(image):
    return image.filter(ImageFilter.GaussianBlur(radius=3))

# Edge
def edge(image):
    return image.filter(ImageFilter.EDGE_ENHANCE_MORE)

# Solar
def solar(image):
    return ImageOps.solarize(image, threshold=80)
