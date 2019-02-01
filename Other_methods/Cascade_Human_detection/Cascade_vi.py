import cv2
import time


video = '../../MP4/Originals/6.mp4'
image = '../../MP4/Data/0.png'
haarcascade_XML = 'haarcascade_fullbody.xml'

person_cascade = cv2.CascadeClassifier(haarcascade_XML)

cap = cv2.VideoCapture(video)

while True:
    r, frame = cap.read()
    if r:
        start_time = time.time()
        frame = cv2.resize(frame, (400, 500))  # Downscale to improve frame rate
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # Haar-cascade classifier needs a grayscale image
        rects = person_cascade.detectMultiScale(gray_frame)

        end_time = time.time()
        # print("Elapsed Time:", end_time - start_time)

        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("preview", frame)

    k = cv2.waitKey(1)
    if k & 0xFF == ord("q"):  # Exit condition
        break
