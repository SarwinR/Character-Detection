import cv2 as cv

class Vision:

    detector_model = None

    def __init__(self, model_path):
        self.detector_model = cv.CascadeClassifier(model_path)

    def locate_object(self, image):
        rectangles = self.detector_model.detectMultiScale(image)
        return rectangles

    @staticmethod
    def draw_rectangles(image, rectangles):
        line_color = (162, 40, 255)
        line_type = cv.LINE_4

        for (x, y, w, h) in rectangles:
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            cv.rectangle(image, top_left, bottom_right, line_color, lineType=line_type)

        return image
