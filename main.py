import cv2 as cv
from time import time
from windowcapture import WindowCapture
from vision import Vision

wincap = WindowCapture('Destiny 2')
detector = Vision('DetectionModel/Destiny2/cascade.xml')

loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    screenshot = cv.Canny(screenshot, threshold1=340, threshold2=350)

    rectangles = detector.locate_object(screenshot)
    detection_image = detector.draw_rectangles(screenshot, rectangles)

    cv.imshow('Window Capture', detection_image)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
