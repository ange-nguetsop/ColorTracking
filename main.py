import cv2
import numpy as np

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Color_Tracking.mp4', fourcc, 25, (width, height))

while True:
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Range of blue
    blue = np.uint8([[[0,0,255]]])
    blue_hsv = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([blue_hsv[0][0][0] - 20,50,50])
    upper_blue = np.array([blue_hsv[0][0][0] + 20,255,255])
    
    #Range of red
    red = np.uint8([[[255,0,0]]])
    red_hsv = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    lower_red = np.array([red_hsv[0][0][0] - 20, 50, 50])
    upper_red = np.array([red_hsv[0][0][0] + 20, 255, 255])
    
    #Range of green
    green = np.uint8([[[0,255,0]]])
    green_hsv = cv2.cvtColor(green, cv2.COLOR_BGR2HSV) 
    lower_green = np.array([green_hsv[0][0][0] - 20, 50, 50])
    upper_green = np.array([green_hsv[0][0][0] + 20, 255, 255])
    
    # Threshold the HSV image to get the desired colors
    mask_red = cv2.inRange(hsv,lower_red,upper_red)
    mask_green = cv2.inRange(hsv,lower_green,upper_green)
    mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)
    
    # mask for all the colors
    mask_combined = cv2.bitwise_or(mask_blue, mask_red)
    mask_combined = cv2.bitwise_or(mask_combined, mask_green)
    
    res = cv2.bitwise_and(frame,frame,mask = mask_combined)
    out.write(res)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
        
cap.release()        
cv2.destroyAllWindows()
