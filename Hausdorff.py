import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def HausDimIm(image):
    # Capture the image and convert it to gray
    f = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2GRAY)
    # Save the length in x and y
    (sizeX, sizeY) = f.shape
    # Set the number and the size of the boxes
    boxes = [2, 4, 8, 16, 32, 64]

    numberOfBoxes = len(boxes)
    # Create an array to save the least number of distinct copies of the boxes in the scale r
    NR = []

    # Find the Hausdorff dimension by th Box Counting Algorithm
    for box in boxes:
        sizeBoxX = int(math.floor(sizeX / box))
        sizeBoxY = int(math.floor(sizeY / box))
        counterOfBoxes = 0
        for i in range(0, box):
            xi = i * sizeBoxX
            xf = (i + 1) * sizeBoxX
            for j in range(0, box):
                yi = j * sizeBoxY
                yf = (j + 1) * sizeBoxY
                boxCaptured = f[yi:yf, xi:xf]
                counterOfBoxes += math.ceil((float(np.max(boxCaptured)) - float(np.min(boxCaptured))) / float(sizeBoxX)) \
                                  + 1
                # counterOfBoxes += math.ceil((np.max(boxCaptured)) / float(sizeBoxX)) - \
                #                   math.ceil((np.min(boxCaptured)) / float(sizeBoxX)) + 1
        NR.append(counterOfBoxes)
    x = []
    y = []
    for cont in range(0, len(NR)):
        x.append(math.log(boxes[cont]))
        y.append(math.log(NR[cont]))

    z = np.polyfit(x, y, 1)

    # print 'The approximated Hausdorff dimension is: ', z[0]
    return z[0]

def HausDimImEq(image):
    # Capture the image and convert it to gray
    f = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2GRAY)
    f = cv2.equalizeHist(f)
    # Save the length in x and y
    (sizeX, sizeY) = f.shape
    # Set the number and the size of the boxes
    # boxes = [2, 4, 8, 16, 32, 64]
    boxes = [2, 4, 8, 16]
    # Create an array to save the least number of distinct copies of the boxes in the scale r
    NR = []
    # Find the Hausdorff dimension by th Box Counting Algorithm
    # print len(boxes)
    for box in boxes:
        sizeBoxX = int(math.floor(sizeX / box))
        sizeBoxY = int(math.floor(sizeY / box))
        counterOfBoxes = 0
        for i in range(0, box):
            xi = i * sizeBoxX
            xf = (i + 1) * sizeBoxX
            for j in range(0, box):
                yi = j * sizeBoxY
                yf = (j + 1) * sizeBoxY
                boxCaptured = f[yi:yf, xi:xf]
                counterOfBoxes += math.ceil((float(np.max(boxCaptured)) - float(np.min(boxCaptured))) / float(sizeBoxX)) \
                                  + 1
                # counterOfBoxes += math.ceil((float(np.max(boxCaptured)) - float(np.min(boxCaptured))) / float(sizeBoxX)) \
                #                   + 1
        NR.append(counterOfBoxes)
    x = []
    y = []
    for cont in range(0, len(NR)):
        x.append(math.log(boxes[cont]))
        y.append(math.log(NR[cont]))

    z = np.polyfit(x, y, 1)

    # print 'The approximated Hausdorff dimension is: ', z[0]
    return z[0]

def HausDimViEq(image):
    # Capture the image and convert it to gray
    f = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    f = cv2.equalizeHist(f)
    # Save the length in x and y
    (sizeX, sizeY) = f.shape
    # Set the number and the size of the boxes
    # boxes = [2, 4, 8, 16, 32, 64]
    boxes = [2, 4, 8, 16]
    # Create an array to save the least number of distinct copies of the boxes in the scale r
    NR = []
    # Find the Hausdorff dimension by th Box Counting Algorithm
    # print len(boxes)
    for box in boxes:
        sizeBoxX = int(math.floor(sizeX / box))
        sizeBoxY = int(math.floor(sizeY / box))
        counterOfBoxes = 0
        for i in range(0, box):
            xi = i * sizeBoxX
            xf = (i + 1) * sizeBoxX
            for j in range(0, box):
                yi = j * sizeBoxY
                yf = (j + 1) * sizeBoxY
                boxCaptured = f[yi:yf, xi:xf]
                counterOfBoxes += math.ceil((float(np.max(boxCaptured)) - float(np.min(boxCaptured))) / float(sizeBoxX)) \
                                  + 1
        NR.append(counterOfBoxes)
    x = []
    y = []
    for cont in range(0, len(NR)):
        x.append(math.log(boxes[cont]))
        y.append(math.log(NR[cont]))

    z = np.polyfit(x, y, 1)

    # print 'The approximated Hausdorff dimension is: ', z[0]
    return z[0]

def HausDimVi(image):
    f = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (sizeX, sizeY) = f.shape
    # boxes = [16, 32, 64]
    # boxes = [2, 4, 8, 16]
    boxes = [125]
    # boxes = [60]
    NR = []
    for box in boxes:
        sizeBoxX = int(math.floor(sizeX / box))
        sizeBoxY = int(math.floor(sizeY / box))
        counterOfBoxes = 0
        for i in range(0, box):
            xi = i * sizeBoxX
            xf = (i + 1) * sizeBoxX
            for j in range(0, box):
                yi = j * sizeBoxY
                yf = (j + 1) * sizeBoxY
                boxCaptured = f[yi:yf, xi:xf]

                counterOfBoxes += math.ceil((float(np.max(boxCaptured)) - float(np.min(boxCaptured)))/ float(sizeBoxX)) \
                                   + 1

        NR.append(counterOfBoxes)
    x = []
    y = []
    for cont in range(0, len(NR)):
        x.append(math.log(boxes[cont]))
        y.append(math.log(NR[cont]))


    res = []
    # z = np.polyfit(x, y, 1)
    # for i in range(0,len(x)):
    #     res.append(y[i]/x[i])
    # plt.plot(res)
    #
    # plt.xlabel('time (s)')
    # plt.ylabel('voltage (mV)')
    # plt.title('About as simple as it gets, folks')
    # plt.grid(True)
    # plt.savefig("test.png")
    # plt.show()
    return y[0]/x[0]
    # return z[0]