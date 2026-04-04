import numpy as np

def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    return [[0.299 * r + 0.587 * g + 0.114 * b for r, g, b in row] for row in image]