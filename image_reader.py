import cv2

#img = cv2.imread('laser.png')
#img = cv2.imread('test1.jpg')
img = cv2.imread('test_images/test2.jpg')
width = 400
heigth = 180
dim = (width, heigth)
t_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(t_img, cv2.COLOR_BGR2GRAY)
b, g, r = cv2.split(t_img)
cv2.imwrite('rgb/red.png', r)
cv2.imwrite('rgb/green.png', g)
cv2.imwrite('rgb/blue.png', b)

cv2.imshow('image', t_img)
cv2.imshow('rgb/red.png', r)
cv2.imshow('rgb/green.png', g)
cv2.imshow('rgb/blue.png', b)
cv2.imshow('gray', gray)
cv2.waitKey(0)

cv2.destroyAllWindows()