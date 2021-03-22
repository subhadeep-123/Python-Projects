import os
import sys
import pytube
import logging
import getpass
from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from tkinter.messagebox import askyesno, showinfo
from tkinter.messagebox import showerror


root = Tk()
root.title("Youtube Downloaded")
root.geometry("400x400")
root.iconbitmap('assets\icon.ico')

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s  |  %(name)s  |  %(message)s')
logger.setLevel(10)

# Initial Directory for the Explorer window to open
initialdirname = None
if sys.platform.startswith('win32'):
    initialdirname = f"C:/Users/{getpass.getuser()}/Desktop"
if sys.platform.startswith('linux'):
    initialdirname = f"/home/{getpass.getuser()}/Desktop"


def download():
    logger.critical(f"Link Recieved - {link.get()}")
    if not link.get():
        showerror("Link Error", "No Video URL Specified")
    else:
        try:
            yt = YouTube(link.get())
        except pytube.exceptions.VideoUnavailable as err:
            logger.error(err)
            showerror("Error", "This Video Is Not Available")
        except pytube.exceptions.RegexMatchError as rerror:
            logger.error(rerror)
            showerror("Error", "Wrong Video URL Pattern")
        except Exception as e:
            logger.error(f"Error Occurred - {e}")
        else:
            resp = askyesno("Answer", "Do you want to download this video??")
            if resp:
                path = filedialog.askdirectory(title='Select and Directory')
                logger.info(
                    f"Selected Directory - {os.path.split(path)[1]}")
                yo = yt.streams.first().download(path)
                if yo:
                    showinfo(
                        "Success", f"{os.path.split(yo)[1]}, downloaded successfully.")
            else:
                logger.warning("Operation Cancelled by the User.")


def selectFile():
    global file
    links = None
    file = filedialog.askopenfilenames(title='Select a File', filetype=(
        ("Text File", "*.txt"),),
        initialdir=initialdirname
    )
    logger.debug(f"Selected File - {file}")
    path = filedialog.askdirectory(title='Select and Directory')
    logger.info(
        f"Selected Directory - {os.path.split(path)[1]}")
    with open(file[0], 'r') as f:
        links = f.read().split(',')
    logger.debug(links)
    resp = askyesno("Answer", "Do you want to download this videos??")
    if resp:
        for i in links:
            logger.critical(f"Link Recieved - {i}")
            try:
                yt = YouTube(i)
            except pytube.exceptions.VideoUnavailable as err:
                logger.error(err)
                showerror("Error", "This Video Is Not Available")
            except pytube.exceptions.RegexMatchError as rerror:
                logger.error(rerror)
                showerror("Error", "Wrong Video URL Pattern")
            except Exception as e:
                logger.error(f"Error Occurred - {e}")
            else:
                yo = yt.streams.first().download(path)
                if yo:
                    showinfo(
                        "Success", f"{os.path.split(yo)[1]}, downloaded successfully.")
    else:
        logger.warning("Operation Cancelled by the User.")


link = Entry(root, width=50)
link.pack(pady=30)
file = Button(root, text='Select a File.', command=selectFile)
file.pack(pady=2)
downloader = Button(root, text="Download", command=download,
                    width=20, bg='#E06F57')

downloader.pack(pady=5)
if __name__ == '__main__':
    root.mainloop()
