from tkinter import *
import ctypes,os
from tkinter.tix import *
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import askopenfilename


home = Tk()
img = Image.open("images/home.png")
img = ImageTk.PhotoImage(img)
panel = Label(home, image=img)
panel.pack(side="top", fill="both", expand="yes")
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-610)
b= str(lt[1]//2-383)
home.title("Sign2Text")
home.geometry("1243x738+"+a+"+"+b)
home.resizable(0,0)

def web():
    import app
photo = Image.open("images/button.png")
img2 = ImageTk.PhotoImage(photo)
                   
Button(home, highlightthickness = 0, bd = 0,activebackground="#fbfdff", image = img2,command=web).place(x=40,y=530)

home.mainloop()

