import numpy as np
from load_image import ft_load
from PIL import Image


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    path = "landscape.jpg"
    img = ft_load(path)
    arr = np.array(img)

    inverted_arr = 255 - arr
    inverted_img = Image.fromarray(inverted_arr)
    inverted_img.show()


def ft_red(array) -> np.ndarray:
    """
    Remove the other colors to get the red filter.
    """
    path = "landscape.jpg"
    img = ft_load(path)
    arr = np.array(img)

    red_filtered = arr.copy()
    red_filtered[:, :, 1] = 0
    red_filtered[:, :, 2] = 0

    red_image = Image.fromarray(red_filtered)
    red_image.show()


def ft_green(array) -> np.ndarray:
    """
    Remove the other colors to get the green filter.
    """
    path = "landscape.jpg"
    img = ft_load(path)
    arr = np.array(img)

    green_filtered = arr.copy()
    green_filtered[:, :, 0] = 0
    green_filtered[:, :, 2] = 0

    green_image = Image.fromarray(green_filtered)
    green_image.show()


def ft_blue(array) -> np.ndarray:
    """
    Remove the other colors to get the blue filter.
    """
    path = "landscape.jpg"
    img = ft_load(path)
    arr = np.array(img)

    blue_filtered = arr.copy()
    blue_filtered[:, :, 0] = 0
    blue_filtered[:, :, 1] = 0

    blue_image = Image.fromarray(blue_filtered)
    blue_image.show()


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale.
    """
    path = "landscape.jpg"
    img = ft_load(path)

    gray_img = img.convert("L")
    gray_img.show()
