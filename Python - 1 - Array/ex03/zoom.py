from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def zoom():
    """
    Loads an image, zooms into its center, and displays
    only the red channel.

    This function:
    1. Loads 'animal.jpeg' using ft_load
    2. Crops a 400x400 pixel square from the center
    3. Extracts the red channel
    4. Displays the resulting grayscale image with matplotlib

    Raises:
        TypeError: If the loaded object is not a PIL Image
        Exception: Any other error during image processing

    Returns:
        None: Displays the processed image
    """
    try:
        path = "animal.jpeg"
        img = ft_load(path)

        if not isinstance(img, Image.Image):
            raise TypeError("Loaded object is not a PIL Image")

        width, height = img.size

        center_x, center_y = width // 2, height // 2
        left = center_x - 200
        upper = center_y - 200
        right = center_x + 200
        lower = center_y + 200
        zoomed_img = img.crop((left, upper, right, lower))

        zoomed_arr = np.array(zoomed_img)

        red_channel = zoomed_arr[:, :, 0]
        print(f"New shape after slicing: {red_channel.shape}")
        print(red_channel)

        plt.imshow(red_channel, cmap='gray')
        plt.title("Zoomed Image (Red channel)")
        plt.axis('on')
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    zoom()
