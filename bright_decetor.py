import cv2
import numpy as np
import argparse
import math

#arguments parsing, when run in cmd line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to image file")
ap.add_argument("-r", "--radius", type = int, help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())

class image_tools(object):
    def resize_image(self, image, width=640, heigth=480):
        dim = (width, heigth)
        resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        return resized_image

    def load_image(self, path):
        image = cv2.imread(path)
        return image

    def calculate_range(self, maxLoc, focal_angle=55.7, laser_dist=30.0, angle=28):
        tan_alpha = math.tan(angle * 3.14 / 180)
        focal = focal_angle * 3.14 / 180
        focal_px = 320 / math.tan(focal / 2)
        distance = float(laser_dist / float(tan_alpha + (maxLoc[0] - 320) / focal_px))
        return abs(distance)/10

    def prepare_blurred_gray(self, image, RADIUS_BLUR=3):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.GaussianBlur(image, (RADIUS_BLUR, RADIUS_BLUR), 0)
        return image

    def prepare_image(self, path):
        image = self.load_image(path)
        image = self.resize_image(image)
        image = self.prepare_blurred_gray(image)
        return image

    def calculateDist(self, image):
        RADIUS_DETECTION = 5
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(image)
        cv2.circle(image, maxLoc, RADIUS_DETECTION, (255, 0, 0), 2)
        dist = self.calculate_range(maxLoc)
        print("Distance: ", dist)
        cv2.imshow("Image: ", image)
        cv2.waitKey()
        return dist

    def analyzeImageAndReturnDist(self, path):
        image = self.prepare_image(path)
        return self.calculateDist(image)

#PATH = 'obrazki/pomiar_50cm.jpg'

#b, g, r = cv2.split(image)

#tool = image_tools()
#tool.analyzeImageAndReturnDist(PATH)
