import click as click
import cv2, time, os, sys
from ascii import render


@click.command()
@click.option('--input', prompt='Input image file', help='Input image')
@click.option('--output', default='', help='Output txt (print to console if not set)')
@click.option('--height', default=50, help='ASCII art height (0 for terminal height)')
@click.option('--gradient', default=' .:!/r(l1Z4H9W8$@', help='Symbols for output (from the darkest to brightest)')
@click.option('--font-aspect', default='7/15', help='Symbol aspect (default for Cascadia Code font) Pattern: x/y')
def main(input: str, output: str, height: int, gradient: str, font_aspect: str):
    img = cv2.imread(input)
    frame = img
    frame_h, frame_w, _ = frame.shape
    aspect = frame_w / frame_h

    if height == 0:
        height = os.get_terminal_size().lines

    font_aspect = tuple(map(int, font_aspect.split('/')))
    symbol_aspect = font_aspect[0] / font_aspect[1]

    resolution = (round(height * aspect / symbol_aspect), height)
    frame = cv2.resize(frame, resolution, interpolation=cv2.INTER_AREA)
    art = render(frame, gradient)

    if output != '':
        with open(output, 'w') as f:
            f.write(art)
    else:
        print(art)


if __name__ == '__main__':
    main()