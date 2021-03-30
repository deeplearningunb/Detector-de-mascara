import cv2 as cv
import os

cam = cv.VideoCapture(0)

classifier = cv.CascadeClassifier(f"model.xml")

while True:
    status, frame = cam.read()

    if not status:
        break

    if cv.waitKey(1) & 0xff == ord('q'):
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = classifier.detectMultiScale(gray)

    for x,y,w,h in faces:
        gray_face = gray[y:y+h, x:x+w]

        if gray_face.shape[0] >= 200 and gray_face.shape[1] >= 200:

            cv.rectangle(frame,(x,y),(x+w,x+h),(0,255,0), 3)

            cv.putText(frame,"Um rosto",(x - 20,y + h + 50), cv.FONT_HERSHEY_COMPLEX,0.5, (243,255,0), 2, cv.LINE_AA)

    cv.imshow("Screen",frame)
