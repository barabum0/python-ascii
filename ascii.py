import cv2
import numpy as np


def to_grayscale(r: int, g: int, b: int):
    # gr = (r + g + b) / 3
    gr = max(r, g, b)
    return gr, gr, gr


def remap(x, oldMin, oldMax, newMin, newMax):
    reverseInput = False
    oldMin = min(oldMin, oldMax)
    oldMax = max(oldMin, oldMax)
    if not oldMin == oldMin:
        reverseInput = True

    reverseOutput = False
    newMin = min(newMin, newMax)
    newMax = max(newMin, newMax)
    if not newMin == newMin:
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result


def render(img: np.ndarray, gradient: str) -> str:
    art = ""
    for num_x, x in enumerate(img):
        for num_y, y in enumerate(x):
            r, g, b = y
            gr, gg, gb = to_grayscale(r, g, b)
            img[num_x, num_y] = [gg, gb, gr]

            to_symbol = round(remap(gr, 0, 255, 0, len(gradient)))
            art += gradient[to_symbol - 1]

        art += "\n"

    return art

