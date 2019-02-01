import numpy as np
from Hausdorff import *
from time import gmtime, strftime
import matplotlib.pyplot as plt
from tempfile import TemporaryFile

import cv2


cap = cv2.VideoCapture('./DataSet/' + '6.mp4')
path = './Data/'
samples = 0
plotDim = []
plotDimEq = []
tempDim = []
f = open(path + "data_partial_6v2", "w")

while cap.isOpened():
    ret, frame = cap.read()
    samples += 1
    if frame is None:
        break
    cv2.imshow('frame', frame)
    x = HausDimVi(frame)
    if samples % 60 == 1: # 300
        tempDim.append(x)
        print strftime("%H:%M:%S", gmtime())
        # cv2.imwrite(path + str(int(samples/60)) + '.png', frame)
        # f.write(str(int(samples/60)) + ";" + str(x) + "\n")
    plotDim.append(x)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print 'Hausdorff dimension calaculated'
f = open(path + "data_6v2", "w")
f.write("# x y\n")
np.savetxt(f, plotDim)
print tempDim

cap.release()
cv2.destroyAllWindows()
