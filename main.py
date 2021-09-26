import cv2 as cv
from time import time
from windowcapture import WindowCapture
from vision import Vision

wincap = WindowCapture('Minecraft 1.8')
detector = Vision('')

loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()
    rectangles = detector.locate_object(screenshot)
    detection_image = detector.draw_rectangles(screenshot, rectangles)

    cv.imshow('Window Capture', detection_image)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break