import cv2 as cv
import os
from keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
import numpy as np
from keras.preprocessing import image

cam = cv.VideoCapture(0)

cnn = keras.models.load_model('mask_detector_model')

while True:
    status, frame = cam.read()

    if not status:
        break

    if cv.waitKey(1) & 0xff == ord('q'):
        break

    cv.imwrite('frame.png',frame)

    test_image = image.load_img('frame.png', target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = cnn.predict(test_image)
    if result[0][0] == 1:
        prediction = 'COM mascara'
        cv.rectangle(frame,(150,15),(500,85),(255,255,255), -1)
        cv.putText(frame,prediction,(0 + 200,0 + 0 + 50), cv.FONT_HERSHEY_COMPLEX,1, (56,142,72), 2, cv.LINE_AA)
    else:
        prediction = 'SEM mascara'
        cv.rectangle(frame,(150,15),(500,85),(255,255,255), -1)
        cv.putText(frame,prediction,(0 + 200,0 + 0 + 50), cv.FONT_HERSHEY_COMPLEX,1,(0,40,255) , 2, cv.LINE_AA)

    cv.imshow("Screen",frame)
