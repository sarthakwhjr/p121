import cv2
import time
import numpy as np
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("output.avi",fourcc,20,(200,200))
capture=cv2.VideoCapture(0)
time.sleep(2)
count=0
background=0
for i in range(60):
    returnV,background=capture.read()
background=np.flip(background,axis=1)

while(capture.isOpened()):
    returnV,img=capture.read()
    if not(returnV):
        break
    img=np.flip(img,axis=1)
    
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerblack=np.array([104,153,70])
    upperblack=np.array([30,30,0])
    mask1=cv2.inRange(hsv,lowerblack,upperblack)
    lowerblack=np.array([104,153,70])
    upperblack=np.array([30,30,0])
    mask2=cv2.inRange(hsv,lowerblack,upperblack)
    mask1+=mask2
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask2=cv2.bitwise_not(mask1)
    notblackone=cv2.bitwise_and(img,img,mask=mask2)
    blackone=cv2.bitwise_and(background,background,mask=mask1)
    finaloutput=cv2.addWeighted(notblackone,1,blackone,1,0)
    out.write(finaloutput)
    cv2.imshow("magic",finaloutput)
    cv2.waitKey(1)
 
capture.release()
out.release()
cv2.destroyAllWindows()    