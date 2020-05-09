import os
import cv2
import imutils
import pytesseract
import numpy as np
from picamera import PiCamera
from time import sleep

camera = PiCamera()
characters = 8

def main(length):
    for i in range(5):
        take_picture(grayify, length)

def grayify(file, length):
    print('extracting..')

    # Opening the image
    img_color = cv2.imread(file, 1) # options: 1, -1 and 0. 0 = grayscale
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY) #convert to grey scale
    
    # Removing the unwanted details from an image with blur
    # destination_image = cv2.bilateralFilter(source_image, diameter of pixel, sigmaColor, sigmaSpace)
    img = cv2.bilateralFilter(img, 11, 17, 17)
    
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
        result = extract(text, length)
        if result:
            print(result)

    except:
        pass

    cv2.imwrite('temp/edged.jpg', edged)
    cv2.imwrite('temp/color.jpg', img_color)
    cv2.imwrite('temp/masked.jpg', new_image)
    cv2.imwrite('temp/cropped.jpg', cropped)

def extract(text, length):
    text = text.split()
    license_plate = ''
    
    for found in text:
        if len(found) == length:
            license_plate = found
    
    return license_plate

def take_picture(callback, length):
    file = 'temp/image.jpg'
    camera.capture(file)
    callback(file, length)
    os.remove('temp/image.jpg')

main(characters)
