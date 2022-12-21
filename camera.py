import click
import cv2, time, os, sys
from ascii import render, remap


@click.command()
@click.option('--input', default=0, help='Camera index')
@click.option('--height', default=50, help='ASCII art height (default for terminal height)')
@click.option('--gradient', default=' .:!/r(l1Z4H9W8$@', help='Symbols for output (from the darkest to brightest) (default is ok)')
@click.option('--font-aspect', default='7/15', help='Symbol aspect (default for Cascadia Code font) Pattern: x/y')
def main(input: int, height: int, gradient: str, font_aspect: str):
    cam = cv2.VideoCapture(input)

    font_aspect = tuple(map(int, font_aspect.split('/')))

    heightChange = (height == 0)


    while True:
        ret, frame = cam.read()

        frame_h, frame_w, _ = frame.shape
        aspect = frame_w / frame_h

        if heightChange == True:
            height = os.get_terminal_size().lines

        symbol_aspect = font_aspect[0] / font_aspect[1]

        resolution = (round(height * aspect / symbol_aspect), height)
        frame = cv2.resize(frame, resolution, interpolation=cv2.INTER_AREA)
        art = render(frame, gradient)

        sys.stdout.write(art)


if __name__ == '__main__':
    main()
