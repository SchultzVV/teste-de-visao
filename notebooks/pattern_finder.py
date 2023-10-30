import numpy as np
import cv2 

cv2.namedWindow('Track')
cv2.resizeWindow('Track', 700, 512)

def track(x):
    pass

cv2.createTrackbar('hue min', 'Track', 0, 179, track)
cv2.createTrackbar('hue max', 'Track', 179, 179, track)
cv2.createTrackbar('sat min', 'Track', 0, 255, track)
cv2.createTrackbar('sat max', 'Track', 255, 255, track)
cv2.createTrackbar('val min', 'Track', 0, 255, track)
cv2.createTrackbar('val max', 'Track', 255, 255, track)

img = cv2.imread('notebooks/img_q_2/img67.png')
#img = cv2.imread('notebooks/img_q_2/img47.png')

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('img', hsv_img)

while True:
    h_min = cv2.getTrackbarPos('hue min', 'Track')
    h_max = cv2.getTrackbarPos('hue max', 'Track')
    s_min = cv2.getTrackbarPos('sat min', 'Track')
    s_max = cv2.getTrackbarPos('sat max', 'Track')
    val_min = cv2.getTrackbarPos('val min', 'Track')
    val_max = cv2.getTrackbarPos('val max', 'Track')
    print(f'HUE MIN : {h_min} HUE MAX: {h_max} SAT MIN {s_min} SAT MAX {s_max} VAL MAX {val_max} VAL MIN {val_min}')

    lower = np.array([h_min, s_min, val_min])
    uper= np.array([h_max, s_max, val_max])
    mask = cv2.inRange(hsv_img, lower, uper)
    mask2 = cv2.inRange(hsv_img, lower, uper)
    det_obj = cv2.bitwise_and(img, img, mask=mask2)

    cn = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cn) > 0:
        blue_area = max(cn, key=cv2.contourArea)
        (xg, yg, wg, hg) = cv2.boundingRect(blue_area)
        cv2.rectangle(img, (xg, yg), (xg+wg, yg + hg), (0, 255, 0), 3)
        print('object detected')

    cv2.imshow('mask', mask)
    cv2.imshow('img', img)

    if cv2.waitKey(1) &0xFF == ord('q'):
       break