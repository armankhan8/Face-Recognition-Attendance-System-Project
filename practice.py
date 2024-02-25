import cv2
import os
cap = cv2.VideoCapture(0)

imgbackGround = cv2.imread('Resources/background.png')
imgpathModes = 'Resources/Modes'
imgListpath = os.listdir(imgpathModes)
imgcontain = []

for path in imgListpath:
    imgcontain.append(cv2.imread(os.path.join(imgpathModes, path)))

while True:
    succ, img = cap.read()
    imgbackGround[44:44+633, 808:808 + 414] = imgcontain[2]
    imgbackGround[162:162+480, 55:55+640] = img
    cv2.imshow("Attendance", imgbackGround)
    # cv2.imshow("Attendance", img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
