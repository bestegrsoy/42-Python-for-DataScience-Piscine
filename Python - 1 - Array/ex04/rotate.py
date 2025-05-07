from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def transpose_image(matrix: list[list[int]]) -> list[list[int]]:
    """
    Manually transpose a 2D list
    """
    transposed = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        transposed.append(new_row)
    return transposed


def rotate():
    """
    Main function to load an image, slice it, convert it to greyscale,
    transpose it manually and plot it.
    """
    try:
        path = "animal.jpeg"
        img = ft_load(path)

        if not isinstance(img, Image.Image):
            raise TypeError("Loaded object is not a PIL Image")

        width, height = img.size

        center_x, center_y = width // 2, height // 2
        left = center_x - 200
        right = center_x + 200
        upper = center_y - 200
        lower = center_y + 200
        croped_img = img.crop((left, upper, right, lower))

        croped_arr = np.array(croped_img)

        grey_channel = croped_arr[:, :, 0]
        print(f"New shape after slicing: {grey_channel.shape}")
        print(grey_channel)

        transpodes = transpose_image(grey_channel.tolist())
        transposed_array = np.array(transpodes)

        print(f"New shape after Transpose: {transposed_array.shape}")
        print(transposed_array)

        plt.imshow(transposed_array, cmap="gray")
        plt.title("Transposed Image")
        plt.axis("on")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    rotate()
