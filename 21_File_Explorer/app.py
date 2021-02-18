import os
import sys
import getpass
import logging
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# Local Imports
import errors

root = Tk()
root.iconbitmap('assets/icon.ico')
root.geometry("544x500")
root.title('File Explorer')

logger = logging.getLogger(__name__)
logging.basicConfig(level=10)
if not os.path.isdir('Logs'):
    os.mkdir('Logs')
FORMAT = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(message)s')
fh = logging.FileHandler('Logs/File.log')
fh.setFormatter(FORMAT)
fh.setLevel(10)
logger.addHandler(fh)

# Initial Directory for the Explorer window to open
initialdirname = None
if sys.platform.startswith('win32'):
    initialdirname = f"C:/Users/{getpass.getuser()}/Desktop"
if sys.platform.startswith('linux'):
    initialdirname = f"/home/{getpass.getuser()}/Desktop"


def OpenDirectory():
    global dirname, in_dir_contents
    dirname = filedialog.askdirectory(title='Select and Directory')
    logger.info(f"Selected Directory - {os.path.split(dirname)[1]}")
    in_dir_contents = os.listdir(dirname)
    for i in in_dir_contents:
        label = Label(root, text=i).pack()


def OpenFile():
    global file
    file = filedialog.askopenfilenames(title='Select a File', filetype=(
        ("Text File", "*.txt"),),
        initialdir=initialdirname
    )
    logger.info(f"Selected File - {file}")


def ReadFile():
    try:
        if file and len(file) > 1:
            raise errors.UnsupportedFotmatError('Cannot Read More than 1 File')
        else:
            with open(file[0], 'r') as f:
                label = Label(root, text=f.read()).pack()
    except Exception as err:
        logger.exception(err)


def write_to_file():
    text = data.get()
    try:
        if file and len(file) > 1:
            raise errors.UnsupportedFotmatError('Cannot Read More than 1 File')
        else:
            if os.path.getsize(file[0]) > 0:
                with open(file[0], 'a') as f:
                    f.write(text)
                logger.debug(
                    'Writing Successfull into the File!! [APPEND MODE]')
            else:
                with open(file[0], 'w') as f:
                    f.write(text)
                logger.debug(
                    'Writing Successfull into the File!! [OVERWRITE MODE]')
    except Exception as err:
        logger.exception(err)


def WriteFile():
    global data
    try:
        if file:
            data = Entry(root, width=30)
            data.pack()
            btn = Button(root, text='WriteToFile',
                         command=write_to_file).pack()
    except NameError as err:
        logger.error(err)
        label = Label(root, text='Neet to Select a File First!!').pack()


def OpenImg():
    global imagename
    imagename = filedialog.askopenfilename(title="Select an Image", filetype=(
        ("PNG", '*.png'),
        ("JPG,JPEG", "*.jpg"),),
        initialdir=initialdirname)
    logger.info(f"Selected Image - {imagename}")
    # Opening the Image in a new window
    if imagename:
        ViewImage()


def ViewImage():
    global img
    new_window = Toplevel()
    new_window.title('Image Viwer')
    new_window.iconbitmap('assets/icon.ico')
    img = ImageTk.PhotoImage(Image.open(imagename))
    label = Label(new_window, image=img).pack()
    btn = Button(new_window, text="Exit Window",
                 command=new_window.destroy).pack()


btn_dir = Button(root, text='OpenDirectory', command=OpenDirectory,
                 padx=100, pady=50).grid(row=0, column=0)  # Done - Alignment

btn_file = Button(root, text="OpenFile", command=OpenFile,
                  padx=100, pady=50).grid(row=0, column=1)  # Done - Alignment

btn_write = Button(root, text='WriteFile', command=WriteFile,
                   padx=115, pady=50).grid(row=1, column=0)  # Done - Alignment

btn_read = Button(root, text='ReadFile', command=ReadFile,
                  padx=101, pady=50).grid(row=1, column=1)  # Done - Alignment

btn_img = Button(root, text='OpenImg', command=OpenImg,
                 padx=112, pady=50).grid(row=2, column=0)  # Done - Alignment

if __name__ == '__main__':
    root.mainloop()
    # TODO Fix Alingmment
