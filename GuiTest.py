import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

counter = 0


def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        label1.config(text="even")
    else:
        label1.config(text="odd")


# root = tk.Tk()
root = tb.Window(themename="superhero")

root.title("test")
# root.iconbitmap('images/codemy.ico')
root.geometry('500x500')

label1 = tb.Label(text="Hello World", font=(
    "Helvetica", 28), bootstyle="default")
label1.pack(pady=20)

button1 = tb.Button(text="Click Me", bootstyle="primary", command=changer)
button1.pack(pady=20)


root.mainloop()
