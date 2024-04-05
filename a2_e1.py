import numpy as np
from PIL import Image


def to_grayscale(pil_image: np.ndarray) -> np.ndarray:
    if pil_image.ndim == 2:
        return pil_image.reshape((1,) + pil_image.shape).astype(pil_image.dtype)

    elif pil_image.ndim == 3 and pil_image.shape[2] == 3:
        pass

    img_normalised = pil_image.astype('float64') / 255

    img_linear = np.where(img_normalised <= 0.04045, img_normalised /
                          12.92, ((img_normalised + 0.055) / 1.055)**2.4)

    Y_linear = np.dot(img_linear, [0.2126, 0.7152, 0.0722])

    # to srbg back
    Y_srgb = np.where(Y_linear <= 0.0031308, Y_linear * 12.92,
                      1.055 * (Y_linear**(1/2.4)) - 0.055)

    grayscale_image = (Y_srgb * 255).clip(0, 255)

    if np.issubdtype(pil_image.dtype, np.integer):
        grayscale_image = np.round(grayscale_image).astype(pil_image.dtype)

        grayscale_image = grayscale_image.reshape(
            (1,) + grayscale_image.shape[:2])

        return grayscale_image

    else:

        raise ValueError("Invalid image shape")


image_path = ''
image = Image.open(image_path)
image_array = np.array(image)

grayscale_image_array = to_grayscale(image_array)
grayscale_image = Image.fromarray(
    np.uint8(grayscale_image_array.reshape(grayscale_image_array.shape[1:])))
grayscale_image.show()
