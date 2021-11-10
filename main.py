import cv2 as cv
import pyautogui
import numpy as np

while True:
    screenshot = pyautogui.screenshot(region=(470,62,394,705))
    opencv_compat_image = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

    found_first_block = False
    for r, i in enumerate(opencv_compat_image[580]):
        if i[0] == 0 and i[1] == 0 and i[2] == 0 and not found_first_block:
            cv.circle(opencv_compat_image,(r+45, 580),18,(0,0,255),-1)
            pyautogui.click(470+r+45, 62+580)
            found_first_block = True

    cv.imshow("Computer Vision", opencv_compat_image)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
