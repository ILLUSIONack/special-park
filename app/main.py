import os
import cv2
import imutils
import pytesseract
import numpy as np
from picamera import PiCamera
from time import sleep

# https://circuitdigest.com/microcontroller-projects/license-plate-recognition-using-raspberry-pi-and-opencv

camera = PiCamera()

def main():
    for i in range(10):
        take_picture(grayify)

def grayify(file):
    print(f'extracting..')
    
    # Opening the image
    img_color = cv2.imread(file, 1) # options: 1, -1 and 0. 0 = grayscale
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY) #convert to grey scale
    
    # Removing the unwanted details from an image with blur
    # destination_image = cv2.bilateralFilter(source_image, diameter of pixel, sigmaColor, sigmaSpace)
    img = cv2.bilateralFilter(img, 11, 25, 25)
    
    # Edge detection with the canny edge method from OpenCV
    # destination_image = cv2.Canny(source_image, thresholdValue 1, thresholdValue 2)
    # The Threshold Vale 1 and Threshold Value 2 are the minimum and maximum threshold values
    edged = cv2.Canny(img, 30, 200) #Perform Edge detection
    
    # Looking for contours on our image
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None
    
    # Loop over contours
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break
    
    if screenCnt is None:
        detected = 0
        print("No contour detected")
    else:
        detected = 1
    
    if detected == 1:
        cv2.drawContours(img_color, [screenCnt], -1, (0, 255, 0), 3)
        
    # Masking the part other than the number plate
    mask = np.zeros(img.shape,np.uint8)
    try:
        new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
        new_image = cv2.bitwise_and(img,img,mask=mask)
    except:
        pass
    
    try:
        # Cropping
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        cropped = img[topx:bottomx+1, topy:bottomy+1]
        
        text = pytesseract.image_to_string(cropped, config='--psm 11')
        print(extract(text))
    except:
        pass

    cv2.imwrite('picture2/haha7.jpg', edged)
    cv2.imwrite('picture2/haha8.jpg', img_color)
    cv2.imwrite('picture2/haha9.jpg', new_image)
    cv2.imwrite('picture2/haha10.jpg', cropped)

def extract(text):
    text = text.split()
    license_plate = ''
    
    for found in text:
        if len(found) > len(license_plate):
            license_plate = found
    
    return license_plate

def take_picture(callback):
    file = 'picture2/image.jpg'
    camera.capture(file)
    callback(file)
    os.remove('picture2/image.jpg')

main()