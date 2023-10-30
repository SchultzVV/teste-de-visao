import cv2
import numpy as np
import base64

def remove_salt_and_pepper(img):
    filtered_image = cv2.medianBlur(img, 5)
    _, encoded_image = cv2.imencode('.jpg', filtered_image)
    image_base64 = base64.b64encode(encoded_image.tobytes()).decode('utf-8')
    return image_base64

def find_silo(img):
    bbox_info = []
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 0, 41])
    uper= np.array([20, 89, 73])
    mask2 = cv2.inRange(hsv_img, lower, uper)
    lower = np.array([0, 10, 43])
    uper= np.array([16, 124, 93])
    lower = np.array([0, 10, 25])
    uper= np.array([16, 140, 84])
    mask2 = cv2.inRange(hsv_img, lower, uper)
    det_obj = cv2.bitwise_and(img, img, mask=mask2)

    cn, h = cv2.findContours(mask2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cn) > 0:
        sorted_contours = sorted(cn, key=cv2.contourArea, reverse=True)[:5]
        for contour in sorted_contours:
            area = cv2.contourArea(contour)
            if area > 60:
                x, y, w, h = cv2.boundingRect(contour)
                bbox_info.append((x, y, w, h))
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                print('Object detected')
    _, encoded_image = cv2.imencode('.jpg', img)
    image_base64 = base64.b64encode(encoded_image.tobytes()).decode('utf-8')

    return image_base64