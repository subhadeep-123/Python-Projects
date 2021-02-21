import os
import sys
import shutil
import getpass
import logging
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Local Imports
import errors

root = Tk()
root.iconbitmap('assets/icon.ico')
root.geometry("544x510")
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


def popup(data=None, mode=None) -> None:
    global write_data, newname, window, newdirname
    window = Toplevel()
    if mode == 'List':
        label0 = Label(
            window, text=f"Selected Directory is:\n{dirname}\n------------------------------").pack()
        for i in data:
            label = Label(window, text=i).pack()
    if mode == 'Read':
        label0 = Label(
            window, text=f"Selected File is:\n{data[0]}\n------------------------------").pack()
        with open(data[0], 'r') as f:
            label = Label(window, text=f.read()).pack()
    if mode == 'Write':
        label0 = Label(
            window, text=f"Selected File is:\n{data[0]}\n------------------------------").pack()
        write_data = Entry(window, width=30)
        write_data.pack()
        btn = Button(window, text='WriteToFile',
                     command=write_to_file).pack()
    if mode == 'RenameFile':
        label0 = Label(
            window, text=f"Selected File is:\n{data[0]}\n------------------------------").pack()
        newname = Entry(window, width=30)
        newname.pack()
        btn = Button(window, text='Save New Name',
                     command=file_rename).pack()
    if mode == 'RenameDir':
        label0 = Label(
            window, text=f"Selected Directory is:\n{data[0]}\n------------------------------").pack()
        newdirname = Entry(window, width=30)
        newdirname.pack()
        btn = Button(window, text='Save New Name',
                     command=dir_rename).pack()
    if mode == 'MakeDir':
        label0 = Label(
            window, text=f"Selected Directory is:\n{data[0]}\n------------------------------").pack()
        newdirname = Entry(window, width=30)
        newdirname.pack()
        btn = Button(window, text='Save Dir Name',
                     command=make_dir).pack()
    if mode == 'MD':
        label0 = Label(
            window, text=f"Selected Directory is:\n{data[0]}\n------------------------------").pack()
        newdirname = Entry(window, width=30)
        newdirname.pack()
        btn = Button(window, text='Save Dir Name',
                     command=move_directory).pack()
    if mode == 'CD':
        label0 = Label(
            window, text=f"Selected Directory is:\n{data[0]}\n------------------------------").pack()
        newdirname = Entry(window, width=30)
        newdirname.pack()
        btn = Button(window, text='Save Dir Name',
                     command=copy_directory).pack()
    btn = Button(window, text='Close', command=window.destroy).pack()


def OpenDirectory():
    global dirname
    dirname = filedialog.askdirectory(title='Select and Directory')
    logger.info(f"Selected Directory - {os.path.split(dirname)[1]}")


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
            popup(file, 'Read')
    except NameError as err:
        logger.error(err)
        messagebox.showerror(title="NotDefined",
                             message="File Not Selected!")
    except Exception as err:
        logging.exception(err)


def write_to_file():
    text = write_data.get()
    try:
        if file and len(file) > 1:
            raise errors.UnsupportedFotmatError('Cannot Read More than 1 File')
        else:
            if os.path.getsize(file[0]) > 0:
                with open(file[0], 'a') as f:
                    f.write('\n')
                    f.write(text)
                logger.debug(
                    'Writing Successfull into the File!! [APPEND MODE]')
                messagebox.showinfo(
                    title='Saved', message='Data Appended to the File')
            else:
                with open(file[0], 'w') as f:
                    f.write(text)
                logger.debug(
                    'Writing Successfull into the File!! [OVERWRITE MODE]')
                messagebox.showinfo(
                    title='Saved', message='Data Overwritten to the File')
    except Exception as err:
        logger.error(f"write_to_file - {err}")
        messagebox.showerror(title="WriteToFileError",
                             message=err)


def WriteFile():
    try:
        if file:
            popup(file, mode='Write')
    except NameError as err:
        logger.error(f"WriteFile - {err}")
        messagebox.showerror(title="NotDefined",
                             message="File Not Selected!")


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


def ListContents():
    global in_dir_contents
    try:
        in_dir_contents = os.listdir(dirname)
        contens = []
        for i in in_dir_contents:
            contens.append(i)
        popup(contens, 'List')
    except Exception as err:
        logger.error(f"ListContents - {err}")
        messagebox.showerror(title="NotDefined",
                             message="Directory Not Selected!")


def ViewImage():
    global img
    new_window = Toplevel()
    new_window.title('Image Viwer')
    new_window.iconbitmap('assets/icon.ico')
    img = ImageTk.PhotoImage(Image.open(imagename))
    label = Label(new_window, image=img).pack()
    btn = Button(new_window, text="Exit Window",
                 command=new_window.destroy).pack()


def RenameFile():
    try:
        if file:
            popup(file, mode='RenameFile')
    except NameError as err:
        logger.error(f"RenameFile - {err}")
        messagebox.showerror(title="NotDefined",
                             message="File Not Selected!")


def file_rename():
    newFileName = newname.get() + '.txt'
    if newFileName:
        val = messagebox.askyesno(
            title='Rename', message='Do You want to continue?')
        if val:
            shutil.copyfile(file[0], os.path.join(
                os.path.split(file[0])[0], newFileName))
            logger.info(f'Copying File Successfule to {newFileName}')
            os.remove(file[0])
            logger.warning(f'Successfully Removed {file[0]}')
            window.destroy
        else:
            logger.critical(
                f'Rename - operation Terminated By the {getpass.getuser()}')


def RenameDirectory():
    try:
        if dirname:
            popup(dirname, mode='RenameDir')
    except NameError as err:
        logger.error(f"RenameDirectory - {err}")
        messagebox.showerror(title="NotDefined",
                             message="Directory Not Selected!")


def dir_rename():
    newDirName = newdirname.get()
    if newDirName:
        val = messagebox.askyesno(
            title='Rename', message='Do You want to continue?')
        if val:
            path = os.path.join(os.path.split(dirname)[0], newDirName)
            shutil.copytree(dirname, path)
            logger.info(f'Copying Directory Contents Successfule to {path}')
            shutil.rmtree(dirname)
            logger.warning(f'Successfully Removed {dirname}')
            window.destroy
        else:
            logger.critical(
                f'Rename - operation Terminated By the {getpass.getuser()}')


def MakeDirectory():
    try:
        if dirname:
            popup(dirname, mode='MakeDir')
    except NameError as err:
        logger.error(f"MakeDirectory - {err}")
        messagebox.showerror(title="NotDefined",
                             message="Parent Directory Not Selected!")


def make_dir():
    newDirName = newdirname.get()
    if newDirName:
        val = messagebox.askyesno(
            title='Rename', message='Do You want to continue?')
        if val:
            path = os.path.join(dirname, newDirName)
            os.mkdir(path)
            logger.debug(f'Successfully Created {path}')
            window.destroy
        else:
            logger.critical(
                f'Rename - operation Terminated By the {getpass.getuser()}')


def DeleteFile():
    try:
        if file:
            os.remove(file[0])
            logger.warning(f'Successfully Removed {file[0]}')
    except NameError as err:
        logger.error(f"DeleteFile - {err}")
        messagebox.showerror(title="NotDefined",
                             message="File Not Selected!")


def DeleteDirectory():
    try:
        if dirname:
            if len(os.listdir(dirname)) == 0:
                os.rmdir(dirname)
            else:
                shutil.rmtree(dirname)
            logger.warning(f'Successfully Removed {dirname}')
    except NameError as err:
        logger.error(f"DeleteDirectory - {err}")
        messagebox.showerror(title="NotDefined",
                             message="Directory Not Selected!")


def MoveFile():
    try:
        if file and dirname:
            newPath = os.path.join(dirname, os.path.split(file[0])[1])
            shutil.copyfile(file[0], newPath)
            logger.info(f'Copying File Successfule to {newPath}')
    except NameError as err:
        logger.error(f"MoveFile - {err}")
        messagebox.showerror(title="NotDefined",
                             message="File/Directory Not Selected!")


def CopyFile():
    try:
        if file and dirname:
            newPath = os.path.join(dirname, os.path.split(file[0])[1])
            shutil.copyfile(file[0], newPath)
            logger.info(f'Copying File Successfule to {newPath}')
    except NameError as err:
        logger.error(f"MoveFile - {err}")
        messagebox.showerror(title="NotDefined",
                             message="File/Directory Not Selected!")


def MoveDirectory():
    global NewDirPath
    try:
        if dirname:
            NewDirPath = filedialog.askdirectory(title='Select and Directory')
            logger.info(f"New Directory - {NewDirPath}")
            logger.info(
                f"Selected Parent Directory - {os.path.split(dirname)[1]}")
            popup(dirname, mode='MD')
    except NameError as err:
        logger.error(f"MoveDirectory - {err}")
        messagebox.showerror(title="NotDefined",
                             message="Parent Directory Not Selected!")


def move_directory():
    NewDirName = newdirname.get()  # New Dir Name
    if NewDirName:
        val = messagebox.askyesno(
            title='Rename', message='Do You want to continue?')
        if val:
            path = os.path.join(NewDirPath, NewDirName)
            shutil.copytree(dirname, path)
            logger.info(f'Copying Directory Contents Successfule to {path}')
            shutil.rmtree(dirname)
            logger.warning(f'Successfully Removed {dirname}')
            window.destroy
        else:
            logger.critical(
                f'Rename - operation Terminated By the {getpass.getuser()}')


def CopyDirectory():
    global NewDirPathCopy
    try:
        if dirname:
            NewDirPathCopy = filedialog.askdirectory(
                title='Select and Directory')
            logger.info(f"New Directory - {NewDirPathCopy}")
            logger.info(
                f"Selected Parent Directory - {os.path.split(dirname)[1]}")
            popup(dirname, mode='CD')
    except NameError as err:
        logger.error(f"MoveDirectory - {err}")
        messagebox.showerror(title="NotDefined",
                             message="Parent Directory Not Selected!")


def copy_directory():
    NewDirName = newdirname.get()  # New Dir Name
    if NewDirName:
        val = messagebox.askyesno(
            title='Rename', message='Do You want to continue?')
        if val:
            path = os.path.join(NewDirPathCopy, NewDirName)
            shutil.copytree(dirname, path)
            logger.info(f'Copying Directory Contents Successfule to {path}')
            window.destroy
        else:
            logger.critical(
                f'Rename - operation Terminated By the {getpass.getuser()}')


btn_dir = Button(root, text='SelectDirectory', command=OpenDirectory,
                 padx=50, pady=30).grid(row=0, column=0, pady=10, padx=10)  # Works

btn_file = Button(root, text="SelectFile", command=OpenFile,
                  padx=50, pady=30).grid(row=0, column=1)  # Works

btn_read = Button(root, text='ReadFile', command=ReadFile,
                  padx=50, pady=30).grid(row=0, column=2)  # Works

btn_write = Button(root, text='WriteFile', command=WriteFile,
                   padx=50, pady=30).grid(row=1, column=0, pady=10)  # Works

btn_img = Button(root, text='OpenImg', command=OpenImg,
                 padx=50, pady=30).grid(row=1, column=1)  # Works

btn_list = Button(root, text="ListFileDir", command=ListContents,
                  padx=50, pady=30).grid(row=1, column=2)   # Works

btn_rename_file = Button(root, text="RenameFile", command=RenameFile,
                         padx=50, pady=30).grid(row=2, column=0, pady=10)  # Works

btn_rename_dir = Button(root, text="RenameDir", command=RenameDirectory,
                        padx=50, pady=30).grid(row=2, column=1)   # Works

btn_mkdir = Button(root, text="MakeDir", command=MakeDirectory,
                   padx=50, pady=30).grid(row=2, column=2)  # Works

btn_delete_dir = Button(root, text="DelDir", command=DeleteDirectory,
                        padx=50, pady=30).grid(row=3, column=1)  # Works

btn_delete_file = Button(root, text="DelFile", command=DeleteFile,
                         padx=50, pady=30).grid(row=3, column=0, pady=10)  # Works

btn_cut_copy = Button(root, text="MvFile", command=MoveFile,
                      padx=50, pady=30).grid(row=3, column=2)  # Works

btn_cut_copy = Button(root, text="MvDir", command=MoveDirectory,
                      padx=50, pady=30).grid(row=4, column=0) # Works

btn_cut_copy = Button(root, text="CpFile", command=CopyFile,
                      padx=50, pady=30).grid(row=4, column=1)  # Works

btn_cut_copy = Button(root, text="CpDir", command=CopyDirectory,
                      padx=50, pady=30).grid(row=4, column=2) # Works
if __name__ == '__main__':
    root.mainloop()
