import cv2
import numpy as np
def getcontours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imdcontour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h=cv2.boundingRect(approx)
            if objCor==3: objectType = "Tri"
            elif objCor==4:
                aspratio = w/float(h)
                if aspratio > 0.95 and aspratio < 1.05: objectType="square"
                else:objectType="Rectangle"
            elif objCor==5: objectType="pentagon"
            elif objCor>5:objectType="circle"
            else:objectType="None"
            cv2.rectangle(imdcontour,(x,y),(x+w,y+h),(0,255,0),3)
            cv2.putText(imdcontour,objectType,(x-8,y-8),cv2.FONT_HERSHEY_COMPLEX,0.5,(50,20,255),2)

path="C:\\Users\\dell\\PycharmProjects\\opecv_proj\\resources/shape2.jpg"
img=cv2.imread(path)
imdcontour = img.copy()

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getcontours(imgCanny)
imgVar = np.vstack((imgGray,imgBlur,imgCanny))
imgVar2 = np.vstack((img,imdcontour))
cv2.imshow("Original",imgVar2)
cv2.imshow("img var",imgVar)



cv2.waitKey(0)