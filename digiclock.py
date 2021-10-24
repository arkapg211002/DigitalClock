'''ARKAPRATIM GHOSH TECHNO MAIN SALTLAKE'''
from tkinter import *
import time
from datetime import date
root = Tk()
root.title("Digital Clock")
root.geometry("600x300")
root.resizable(1,1)
root.maxsize(600,300)
root.minsize(600,300)
label = Label(root, font="radioland 68", bg="black", fg="green", borderwidth=25,relief=SUNKEN)
label.pack(fill=X,anchor="center")
label1 = Label(root, font="radioland 40", bg="black", fg="green", borderwidth=25,relief=SUNKEN)
label1.pack(fill=X,anchor="center")
def digi():
   live = time.strftime("%H:%M:%S")
   lived=date.today()
   label.config(text=live)
   label.after(200, digi)
def day():
   lived=date.today()
   label1.config(text=lived)
   label1.after(100,day)
digi()
day()
root.mainloop()

