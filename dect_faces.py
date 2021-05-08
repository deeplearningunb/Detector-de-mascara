import cv2 as cv
import os
from keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
import numpy as np
from keras.preprocessing import image

cam = cv.VideoCapture(0)

classifier = cv.CascadeClassifier(f"model.xml")

cnn = keras.models.load_model('mask_detector_model')

while True:
    status, frame = cam.read()

    if not status:
        break

    if cv.waitKey(1) & 0xff == ord('q'):
        break

    cv.imwrite('frame.png',frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = classifier.detectMultiScale(gray)

    for x,y,w,h in faces:
        gray_face = gray[y:y+h, x:x+w]

        if gray_face.shape[0] >= 200 and gray_face.shape[1] >= 200:
            test_image = image.load_img('frame.png', target_size = (64, 64))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            result = cnn.predict(test_image)
            if result[0][0] == 1:
                prediction = 'COM mascara'
                cv.rectangle(frame,(x,y),(x+w,x+h),(0,255,0), 3)
                cv.putText(frame,prediction,(x - 20,y + h + 50), cv.FONT_HERSHEY_COMPLEX,0.5, (243,255,0), 2, cv.LINE_AA)
            else:
                prediction = 'SEM mascara'
                cv.rectangle(frame,(x,y),(x+w,x+h),(0,40,255), 3)
                cv.putText(frame,prediction,(x - 20,y + h + 50), cv.FONT_HERSHEY_COMPLEX,0.5, (243,255,0), 2, cv.LINE_AA)

    cv.imshow("Screen",frame)
