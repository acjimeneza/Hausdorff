# Code adapted from:
# https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/
# OpenCV people Counter

import numpy as np
import cv2
import time

prototxt = 'MobileNetSSD_deploy.prototxt.txt'
model = 'MobileNetSSD_deploy.caffemodel'
video = '../../DataSet/6.mp4'

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("[INFO] loading model...")

net = cv2.dnn.readNetFromCaffe(prototxt, model)

imageArray = ['53', '4', '10', '6', '0', '17', '24', '23', '89', '62', '65', '63', '64']


for i in range(len(imageArray)):

    image = '../../MP4/Data/' + imageArray[i] + '.png'

    image = cv2.imread(image)

    start_time = time.time()

    (h, w) = image.shape[:2]

    blob = cv2.dnn.blobFromImage(cv2.resize(image, (500, 600)), 0.019843,  # 0.007843
                                 (500, 600), 0.5)  # 127.5
    # to improve image recognition the blob was adjusted
    net.setInput(blob)
    detections = net.forward()

    people_counter = 0

    for i in np.arange(0, detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence > 0.01:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            people_counter += 1

            cv2.rectangle(image, (startX, startY), (endX, endY), [255, 0, 0], 2)

    end_time = time.time()
    print("Elapsed time:", end_time - start_time)
    print('Total pedestrians = ' + str(people_counter))

    cv2.imshow("Output", image)
    cv2.waitKey(0)


