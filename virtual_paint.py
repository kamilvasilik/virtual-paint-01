# Virtual Painter
#
# - pick colors by moving track bars (everything else should be black in bottom-right image)
#   - press N to define next color
#   - press Q to quit picking color
# - have fun drawing ;-)
#

import cv2
from virtual_paint_library import stackImages, findColor, pickColor, drawOnCanvas

def virtual_paint():
    myPoints = [] # [x, y, [colorB, colorG, colorR]]

    frameWidth = 640
    frameHeigth = 480

    chosenColors = pickColor()

    cam = cv2.VideoCapture(0)
    cam.set(3, frameWidth)
    cam.set(4, frameHeigth)
    cam.set(10, 100) # brightness

    while True:
        success, imgWebflip = cam.read()
        imgWeb = cv2.flip(imgWebflip, 1)
        imgResult = imgWeb.copy()
        newPoints = findColor(imgWeb, imgResult, chosenColors)
        if len(newPoints) != 0:
            for newP in newPoints:
                myPoints.append(newP)
        if len(myPoints) != 0:
            drawOnCanvas(imgResult, myPoints)

        imgStack = stackImages(1, [[imgResult]])
        cv2.imshow("Virtual Paint, press Q to quit", imgStack)

        ch = cv2.waitKey(1)
        if ch == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    virtual_paint()