# Code adapted from:
# https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/
# OpenCV people Counter

import numpy as np
import cv2
import imutils

image = '../../MP4/Data/53.png'
prototxt = 'MobileNetSSD_deploy.prototxt.txt'
model = 'MobileNetSSD_deploy.caffemodel'
video = '../../DataSet/6.mp4'

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

net = cv2.dnn.readNetFromCaffe(prototxt, model)

image = cv2.imread(image)


frame = imutils.resize(image, width=500)

(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(frame, 0.007843, (h, w), 127.5)

print("[INFO] computing object detections...")
net.setInput(blob)
detections = net.forward()

people_counter = 0

for i in np.arange(0, detections.shape[2]):

	confidence = detections[0, 0, i, 2]

	if confidence > 0.20:
		idx = int(detections[0, 0, i, 1])
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")

		people_counter += 1

		cv2.rectangle(image, (startX, startY), (endX, endY), [255, 0, 0], 2)


print('Total pedestrians = ' + str(people_counter))

cv2.imshow("Output", image)
cv2.waitKey(0)


