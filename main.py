import cv2 as cv

img = cv.imread("gogh.jpeg")
print(img.shape)
print(img.size)
print(img.dtype)

cv.line(img, (0, 0), (453, 299), (255, 0, 0), 5)

# font = cv.FONT_HERSHEY_SIMPLEX
# cv.putText(img,'Picsart Academy',(20,280), font, 1.5,(255,255,255),2,cv.LINE_AA)
#
# cv.imshow("Display window", img)
#
# # window is displayed until we press any key
# k = cv.waitKey(0)
# #
# if k == ord("s"):
#     cv.imwrite("starry_night.png", img)

# modify pixel values
img[50, 100] = [2, 127, 18]

px = img[50, 100]

blue = img[50, 100, 0]
# recommended
blue2 = img.item(50, 100, 0)

green = img[50, 100, 1]
# recommended
green2 = img.item(50, 100, 1)

red = img[50, 100, 2]
# recommended
red2 = img.item(50, 100, 2)

moon = img[0:65, 380:445]
# cv.imshow("Display window", moon)
# k = cv.waitKey(0)

img[140:205, 200:265] = moon
cv.imshow("Display window", img)
k = cv.waitKey(0)
