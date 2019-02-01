# Code adapted from:
# https://gist.github.com/madhawav/a951f3790987532d32126a5f437ca28a
# OpenCV people Counter

import cv2
import time
import imutils


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

imageArray = ['53', '4', '10', '6', '0', '17', '24', '23', '89', '62', '65', '63', '64']

pedestrians = 0

for i in range(len(imageArray)):

    image = '../../DataSet/Data/' + imageArray[i] + '.png'

    image = cv2.imread(image)

    # frame = imutils.resize(image, width=1280)

    start_time = time.time()

    frame = cv2.resize(image, (700, 1300))  # Downscale to improve image recognition
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # HOG needs a grayscale image

    rects, weights = hog.detectMultiScale(gray_frame)

    # Measure elapsed time for detections
    end_time = time.time()
    print("Elapsed time:", end_time - start_time)

    for i, (x, y, w, h) in enumerate(rects):
        if weights[i] < 0.1:
            continue
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        pedestrians += 1

    print('Total of pedestrians ' + str(pedestrians))
    pedestrians = 0
    cv2.imshow("preview", frame)
    cv2.waitKey(0)
