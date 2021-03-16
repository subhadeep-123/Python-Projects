import webbrowser
from tkinter import *

root = Tk()
root.geometry("500x200")
root.title("Resumer")
root.iconbitmap('assets\icon.ico')


def pressme():
    webbrowser.open(data.get())
    root.destroy()


data = Entry(root, width=300)
data.pack()
btn = Button(root, text='Open Link', command=pressme).pack()

root.mainloop()
