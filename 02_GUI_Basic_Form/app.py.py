import getpass
import logging
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("450x350")
root.title("Form")
root.iconbitmap('assets/icon_test.ico')

# Logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(10)


def submit():
    global name, age, email, gender, lang, image, img_btn

    resp = messagebox.askyesno("Response", "Do You Want To Submit?")
    if resp:
        name = Label(root, text=f"Name - {a.get()}")
        name.grid(row=8, column=0, sticky=W)

        age = Label(root, text=f"Age - {b.get()}")
        age.grid(row=9, column=0, sticky=W)

        email = Label(root, text=f"EmailId - {c.get()}")
        email.grid(row=10, column=0, sticky=W)

        if r.get() == 0:
            gender = Label(root, text=f"Gender - Male")
            gender.grid(row=11, column=0, sticky=W)
        else:
            gender = Label(root, text=f"Gender - Female")
            gender.grid(row=11, column=0, sticky=W)

        lang = Label(root, text=f"Language - {clicked.get()}")
        lang.grid(row=12, column=0, sticky=W)

        image = Label(root, text="Image- ")
        image.grid(row=13, column=0, sticky=W)
        img_btn = Button(root, text="Open Image", command=open, width=30)
        img_btn.grid(row=13, column=1)

        btn = Button(root, text="Submit", command=submit, state=DISABLED).grid(
            row=7, column=0, pady=20, padx=20)
        root.geometry("600x500")
    else:
        LOGGER.debug("Response was No!")


def clear():
    a.delete(0, END)
    b.delete(0, END)
    c.delete(0, END)
    btn = Button(root, text="Submit", command=submit).grid(
        row=7, column=0, pady=20, padx=20)


def clrscr():
    name.grid_forget()
    age.grid_forget()
    email.grid_forget()
    gender.grid_forget()
    lang.grid_forget()
    image.grid_forget()
    img_btn.destroy()


def upload():
    global filename
    username = getpass.getuser()
    filename = filedialog.askopenfilename(title="Selec an Image", filetype=(
        ("PNG", "*.png"),
        ("JPEG", "*.jpg"),
        ("JPEG", "*.jpeg")),
        initialdir=f"C:/Users/{username}/Desktop"
    )
    upload_btn = Button(root, text="Image Uploaded",
                        command=upload, width=30, state=DISABLED).grid(row=6, column=2)


def open():
    global img
    top = Toplevel()
    top.title("Image Window")
    top.iconbitmap('assets/icon_test.ico')
    img = ImageTk.PhotoImage(Image.open(filename))
    my_label = Label(top, image=img).pack()
    btn = Button(top, text='Close Window', command=top.destroy).pack()


l1 = Label(root, text="Name: ").grid(row=0, column=0)
a = Entry(root, width=30)
a.grid(row=0, column=2, sticky=W)
a.insert(0, "Enter You Name")

l2 = Label(root, text="Age: ").grid(row=1, column=0)
b = Entry(root, width=30)
b.grid(row=1, column=2, sticky=W)
b.insert(0, "Enter You Age")

l3 = Label(root, text="Email").grid(row=2, column=0)
c = Entry(root, width=30)
c.grid(row=2, column=2, sticky=W)
c.insert(0, "Enter You Email")

# RadioButton Variable
r = IntVar()
r.set(0)

l4 = Label(root, text="Gender").grid(row=3, column=0)
Radiobutton(root, text="Male", variable=r, value=0).grid(
    row=3, column=2, sticky=W)
Radiobutton(root, text="Female", variable=r,
            value=1).grid(row=4, column=2, sticky=W)

# Dropdown Options
OPTIONS = [
    "Python",
    "C",
    "C++",
    "Java",
    "Go",
    "Javascript"
]
l5 = Label(root, text="Favroite Language").grid(row=5, column=0)
clicked = StringVar()
clicked.set("---OPTIONS---")
menu = OptionMenu(root, clicked, *OPTIONS)
menu.grid(row=5, column=2, sticky=W)

l5 = Label(root, text="Profile Picture").grid(row=6, column=0)
upload_btn = Button(root, text="Upload Image",
                    command=upload, width=30).grid(row=6, column=2)

# Buttons
btn = Button(root, text="Submit", command=submit).grid(
    row=7, column=0, pady=20, padx=20)
btn2 = Button(root, text="Clear Data", command=clear).grid(
    row=7, column=1, pady=20, padx=20)
btn3 = Button(text="Clear Screen", command=clrscr).grid(
    row=7, column=2, padx=20, pady=20)


if __name__ == '__main__':
    root.mainloop()
