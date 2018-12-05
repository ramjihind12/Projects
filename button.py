import Tkinter
import tkMessageBox
import os

top = Tkinter.Tk()

def helloCallBack():
   os.system("python name1.py")
   

B = Tkinter.Button(top, text ="Register Though Face Detector", command = helloCallBack)
B.pack()
top.mainloop()
