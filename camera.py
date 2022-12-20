import cv2, time, os, sys
from ascii import render, get_html_template


def main():
    cam = cv2.VideoCapture(0)
    gradient = r' .:!/r(l1Z4H9W8$@'

    while True:
        start_time = time.time()

        y = os.get_terminal_size().lines
        ret, frame = cam.read()

        frame_h, frame_w, _ = frame.shape
        aspect = frame_w / frame_h
        symbol_aspect = 7 / 15
        template = get_html_template()

        resolution = (round(y * aspect / symbol_aspect), y)
        frame = cv2.resize(frame, resolution, interpolation=cv2.INTER_AREA)
        art = render(frame, gradient)

        sys.stdout.write(art)


if __name__ == '__main__':
    main()
