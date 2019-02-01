import matplotlib
matplotlib.use('tkAgg')
import Tkinter as tk
import numpy as np
import cv2
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Hausdorff import *


window = tk.Tk()
window.wm_title("Hausdorff Dimension")
window.config(background="#000000")

#Capture video frames
lmain = tk.Label(window)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)


f = Figure(figsize=(5, 3))
a = f.add_subplot(111)
a.set_ylabel('Time(s)')
a.set_title('Dimension')

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=window)
canvas.show()
canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=2)

cap = cv2.VideoCapture('DataSet/6.mp4')
plotDim = np.empty(20000)

samples = 0


def show_frame():
    global samples
    ret, frame = cap.read()

    if frame is not None:
        plotDim[samples] = HausDimVi(frame)
        samples += 1
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        if cap.isOpened():
            lmain.after(3, show_frame)
        if samples%30== 1:
            end = samples / 30
            t = np.arange(0, end, 1.0 / 30)
            a.plot(t, plotDim[0:len(t)], 'RED')
            canvas.show()
    else:
        print np.sum(plotDim)/samples



def on_key_event(event):
    print('you pressed %s' % event.key)


canvas.mpl_connect('key_press_event', on_key_event)


def _quit():
    cap.release()
    cv2.destroyAllWindows()
    window.quit()     # stops mainloop
    window.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = tk.Button( master=window, text='Quit', command=_quit)
button.grid(row = 1, column=0, padx=10, pady=2)

show_frame()  #Display 2
tk.mainloop()
