import cv2
import numpy as np
import argparse
import math

#arguments parsing, when run in cmd line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to image file")
ap.add_argument("-r", "--radius", type = int, help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())

def resizeImage(image, width, heigth):
    width = 800
    heigth = 640
    dim = (width, heigth)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

RADIUS_BLUR = 3
RADIUS_DETECTION = 5
#PATH = 'test_images/test22.jpg'
PATH = 'test_images/pomiar1_6_10_73.png'

#loading image
image = cv2.imread(PATH)

#rescaling
width = 800
heigth = 640
dim = (width, heigth)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

#color to grayscale
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
b, g, r = cv2.split(image)

im = gray

#Gaussian blur
#gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)
gray = cv2.GaussianBlur(im, (RADIUS_BLUR, RADIUS_BLUR), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(im)

#drawing circle with bright region
image = im.copy()
cv2.circle(image, maxLoc, RADIUS_DETECTION, (255,0,0), 2)
print("MaxLoc: ", maxLoc)

laser_dist = 60
alfa = 12
alfa = math.tan(alfa * 3.14 / 180)
ogniskowa_kat = 75.7
ogniskowa_kat = ogniskowa_kat * 3.14 / 180
ogniskowa = 320 / math.tan(ogniskowa_kat/2)
range = float(laser_dist / float(alfa * (maxLoc[0] - 320)/ogniskowa))

print("range: ", abs(range)/10)
cv2.imshow("Imidz", image)
cv2.waitKey()
return range
