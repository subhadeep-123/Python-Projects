import os
from os.path import supports_unicode_filenames
import shutil
import logging
from tkinter import *
from tkinter import filedialog

root = Tk()
root.iconbitmap('assets/icon.ico')
root.geometry("700x500")
root.title('File Explorer')

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=10, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
if not os.path.isdir('Logs'):
    os.mkdir('Logs')
fh = logging.FileHandler('Logs/File.log')
logger.addHandler(fh)


def OpenDirectory():
    global dirname
    dirname = filedialog.askdirectory(title='Select and Directory')
    logger.info(f"Selected Directory - {os.path.split(dirname)[1]}")


def OpenImg():
    global filename
    filename = filedialog.askopenfilename(title="Select a File")
    logger.info(f"Selected File - {os.path.split(filename)[1]}")


def ViewImage():
    pass


def OpenFile():
    pass


def WriteFile():
    pass


def ReadFile():
    pass


btn_dir = Button(root, text='OpenDirectory', command=OpenDirectory).pack()
btn_file = Button(root, text="OpenFile", command=OpenFile).pack()
btn_write = Button(root, text='WriteFile', command=WriteFile).pack
btn_read = Button(root, text='ReadFile', command=ReadFile).pack
btn_img = Button(root, text='OpenImg', command=OpenImg).pack()
btn_img_viwer = Button(root, text='ViewImage', command=ViewImage).pack()

root.mainloop()
