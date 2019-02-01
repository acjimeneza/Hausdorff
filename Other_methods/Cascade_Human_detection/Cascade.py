# Code adapted from:
# https://gist.github.com/madhawav/cd913f68b9405b438833b614ccb49b57
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_fullbody.xml
# Cascade Human Detection

import cv2
import time
import imutils


imageArray = ['53', '4', '10', '6', '0', '17', '24', '23', '89', '62', '65', '63', '64']

haarcascade_XML = 'haarcascade_fullbody.xml'


person_cascade = cv2.CascadeClassifier(haarcascade_XML)

image = '../../DataSet/Data/146.png'


for i in range(len(imageArray)):

    image = '../../MP4/Data/' + imageArray[i] + '.png'

    image = cv2.imread(image)

    frame = imutils.resize(image, width=500)
    # frame = cv2.resize(image, (700, 1200))

    start_time = time.time()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # Haar-cascade classifier needs a grayscale image

    rects = person_cascade.detectMultiScale(gray_frame)

    end_time = time.time()

    print("Elapsed Time:", end_time - start_time)

    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    print('Total of pedestrians ' + str(len(rects)))

    cv2.imshow("preview", frame)
    cv2.waitKey(0)


