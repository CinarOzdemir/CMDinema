import sys
import os
import cv2 as cv
import time
import numpy as np

characters = " .'-:,~;!/*+#$@█"

char_array = np.array(list(characters))


def frameToAscii(frame):
    indices = (frame // (256 / len(characters))).astype(int)
    ascii_matrix = char_array[indices]
    pic = "\n" + "\n".join(["".join(row) for row in ascii_matrix])
    return pic


if len(sys.argv) == 2:
    video = cv.VideoCapture(sys.argv[1])
else:
    video = cv.VideoCapture(0)

success, frame = video.read()

if not success:
    print("Error in the source")
    exit()

# Constants to do math with
try:
    TERMINAL_WIDTH = os.get_terminal_size()[0] // 2
    TERMINAL_HEIGHT = os.get_terminal_size()[1]
except OSError:
    TERMINAL_WIDTH = 80 // 2
    TERMINAL_HEIGHT = 24

SOURCE_WIDTH = len(frame[0])
SOURCE_HEIGHT = len(frame)
SOURCE_FPS = video.get(cv.CAP_PROP_FPS)

# Aspect Ratio math to fit exactly in the terminal
if SOURCE_WIDTH / SOURCE_HEIGHT * TERMINAL_HEIGHT < TERMINAL_WIDTH:
    RESIZE_WIDTH = round(TERMINAL_HEIGHT * SOURCE_WIDTH / SOURCE_HEIGHT)
    RESIZE_HEIGHT = TERMINAL_HEIGHT
else:
    RESIZE_WIDTH = TERMINAL_WIDTH
    RESIZE_HEIGHT = round(TERMINAL_WIDTH / SOURCE_WIDTH * SOURCE_HEIGHT)


# Number of times to put a new line before printing the new frame
newLineCount = TERMINAL_HEIGHT - RESIZE_HEIGHT

frameCount = 1
START_TIME = time.time()

while True:
    if not success:
        print("\nVideo Completed!")
        break

    targetTime = START_TIME + frameCount / SOURCE_FPS
    currentTime = time.time()

    if currentTime > targetTime:
        success, frame = video.read()
        frameCount += 1
        continue

    print(frameToAscii(cv.cvtColor(cv.resize(frame, (RESIZE_WIDTH * 2,
          RESIZE_HEIGHT)), cv.COLOR_BGR2GRAY)) + "\n" * newLineCount, end="")

    targetTime = START_TIME + frameCount / SOURCE_FPS
    currentTime = time.time()
    waitTime = targetTime - currentTime

    frameCount += 1

    cv.waitKey(max(1, int(waitTime * 1000)))

    success, frame = video.read()
