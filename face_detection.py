import cv2
#androidcam = "http://100.73.139.152:4747/video"
#vidpath = "C:\\Users\\dell\\PycharmProjects\\opecv_proj\\resources/vid2.mp4"
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

while True:
    success, vid= cap.read()
    imgGray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (255, 0, 0), 2)


    cv2.imshow("video",vid)


    if cv2.waitKey(1) & 0xFF ==ord('q'):

        break
cv2.destroyAllWindows()