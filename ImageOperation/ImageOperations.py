import cv2
import imutils
import numpy as np


class EdgeDetection:
    __path_of_image = None
    __image_with_borders = None
    @classmethod
    def __init__(self, path_of_image):
        self.path_of_image = path_of_image
        image, edged = self.__convertImageByCanny()
        self.image_with_borders = self.__drawRectangularLineAroundEdges(edged)

    def __convertImageByCanny(self):
        image = cv2.imread(self.path_of_image, 500)
        ratio = image.shape[0] / 500.0
        orig = image.copy()
        image = imutils.resize(image, height=500)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        edged = cv2.Canny(gray, 100, 100)
        return image, edged

    def __drawRectangularLineAroundEdges(self, cannyEdgeImage):
        image = cv2.imread(self.path_of_image,500)
        pts = np.argwhere(cannyEdgeImage > 0)
        y1, x1 = pts.min(axis=0)
        y2, x2 = pts.max(axis=0)
        cropped = image[y1:y2, x1:x2]
        cv2.imwrite("cropp.png", cropped)
        tagged = cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3, cv2.LINE_AA)
        return tagged

    def getBorderImage(self):
        image = cv2.imshow("Edged", self.image_with_borders)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return image
