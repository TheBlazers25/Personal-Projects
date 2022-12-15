import math
import cv2
import numpy as np
import pywinauto
from PIL import ImageGrab

def find_and_shoot_birds():
    """ Captures screen, template matches birds and clicks the matched location """


screenTOP = 700
screenBOT = 800
screenLFT = 600
screenRGT = 1320

template = cv2.imread('blue.png', 0)
template2 = cv2.imread('red.png', 0)
template_w, template_h = template.shape[::-1]
template_w2, template_h2 = template2.shape[::-1]

framecount = 0
while True:

    framecount += 1
    if ((framecount % 1) != 0):
        continue

    # Read screen
    frame_bgr = np.array(ImageGrab.grab(bbox=(screenLFT, screenTOP, screenRGT, screenBOT)))

    # Convert to gray
    frame_gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)

    # Apply template Matching
    bird_candidates = cv2.matchTemplate(image=frame_gray, templ=template, method=cv2.TM_CCOEFF_NORMED)
    definite_birds = np.where(bird_candidates >= 0.7)

    bird_candidates2 = cv2.matchTemplate(image=frame_gray, templ=template2, method=cv2.TM_CCOEFF_NORMED)
    definite_birds2 = np.where(bird_candidates2 >= 0.7)

    for bird in zip(*definite_birds[::-1]):
        cv2.circle(img=frame_bgr, center=(int(bird[0] + template_w / 2), int(bird[1] + template_h / 2)),
                   radius=int(template_h / 2), color=(255, 0, 0), thickness=2)
        cv2.drawMarker(img=frame_bgr, position=(int(bird[0] + template_w / 2), int(bird[1] + template_h / 2)),
                       color=(255, 0, 0), markerType=cv2.MARKER_CROSS, markerSize=30, thickness=2, line_type=cv2.LINE_4)

        pywinauto.mouse.click(button='left', coords=(0, 0))

    for bird in zip(*definite_birds2[::-1]):
        cv2.circle(img=frame_bgr, center=(int(bird[0] + template_w2 / 2), int(bird[1] + template_h2 / 2)),
                   radius=int(template_h2 / 2), color=(255, 0, 0), thickness=2)
        cv2.drawMarker(img=frame_bgr, position=(int(bird[0] + template_w2 / 2), int(bird[1] + template_h2 / 2)),
                       color=(255, 0, 0), markerType=cv2.MARKER_CROSS, markerSize=30, thickness=2, line_type=cv2.LINE_4)

        pywinauto.mouse.click(button='right', coords=(0, 0))

    cv2.imshow('Duck Hunt', cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB))

    if (cv2.waitKey(30) == 27):
        cv2.destroyAllWindows()
        break