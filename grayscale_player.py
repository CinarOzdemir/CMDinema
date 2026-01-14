import sys
import os
import cv2 as cv
import time

characters = " .'-:,~;!/*+#$@█"

# Turns a frame to ASCII art based on terminal dimensions
def frameToAscii(frame) -> str:
    HEIGHT = len(frame)
    WIDTH = len(frame[0])
    pic = [" "] * ((WIDTH + 1) * HEIGHT)

    for row in range(0, len(frame)):

        pic[row * (WIDTH + 1)] = "\n"

        for column in range(0, len(frame[0])):
            brightness = frame[row][column]
            pic[row * (WIDTH + 1) + column + 1] = characters[int(brightness // (256 / len(characters)))] # Map brightness to a character

    return ''.join(pic)


if len(sys.argv) == 2:
    video = cv.VideoCapture(sys.argv[1])
else:
    video = cv.VideoCapture(0)

success, frame = video.read()

if not success:
    print("Error in the source")
    exit()

# Constants to do math with
TERMINAL_WIDTH = os.get_terminal_size()[0] // 2
TERMINAL_HEIGHT = os.get_terminal_size()[1]

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

    print(frameToAscii(cv.cvtColor(cv.resize(frame, (RESIZE_WIDTH * 2,
          RESIZE_HEIGHT)), cv.COLOR_BGR2GRAY)) + "\n"*newLineCount, end="")

    targetTime = START_TIME + frameCount / SOURCE_FPS
    currentTime = time.time()
    waitTime = targetTime - currentTime

    frameCount += 1

    cv.waitKey(max(1, int(waitTime * 1000)))

    success, frame = video.read()
