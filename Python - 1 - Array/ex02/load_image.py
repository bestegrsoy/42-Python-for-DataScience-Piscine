import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the given path, prints its shape,
    and returns its pixel data as a numpy array in RGB format.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: 3D numpy array representing the RGB image.
    """
    try:
        with Image.open(path) as img:
            if img.format not in ["JPEG", "JPG"]:
                raise ValueError("Only JPEG and JPG formats are supported.")
            img = img.convert("RGB")
            data = np.array(img)
            print(f"The shape of image is : {data.shape}")
            return data
    except Exception as e:
        print(f"Error: {e}")
        return None
