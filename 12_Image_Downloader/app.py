import os
import sys
import shutil
import getpass
import logging
import requests
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import askyesno, showinfo
from tkinter.messagebox import showerror


root = Tk()
root.title("Image Downloader")
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
    imgLink = link.get()
    logger.info(f"Image Link Recived - {imgLink}")
    if not link.get():
        showerror("Link Error", "No Video URL Specified")
    else:
        filename = imgLink.split('/')[-1]
        logger.debug(f'Image File Name - {filename}')
        try:
            # Open the url image, set stream to True, this will return the stream content.
            r = requests.get(imgLink, stream=True)
        except requests.exceptions.MissingSchema as err:
            logger.error(err)
            showerror(f"Error Occurred - {err}")
        except Exception as e:
            logger.error(e)
            showerror(f"Error Occurred - {e}")
        else:
            resp = askyesno("Answer", "Do you want to download this video??")
            if resp:
                # Check if the image was retrieved successfully
                if r.status_code == 200:
                    path = filedialog.askdirectory(
                        title='Select and Directory')
                    logger.info(
                        f"Selected Directory - {os.path.split(path)[1]}")
                    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                    r.raw.decode_content = True
                    # Open a local file with wb ( write binary ) permission.
                    with open(os.path.join(path, filename), 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                        logger.debug(
                            f"Image Downloaded Sucessfuly - {filename}")
                    showinfo(
                        "Success", f"{filename}, downloaded successfully.")
                else:
                    logger.critical('Image Couldn\'t be retreived')
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
    resp = askyesno("Answer", "Do you want to download this Images?")
    if resp:
        for i in links:
            logger.info(f"Link Recieved - {i}")
            filename = i.split('/')[-1]
            logger.debug(f'Image File Name - {filename}')
            try:
                r = requests.get(i, stream=True)
            except requests.exceptions.MissingSchema as err:
                logger.error(err)
                showerror(f"Error Occurred - {err}")
            except Exception as e:
                logger.error(e)
                showerror(f"Error Occurred - {e}")
            else:
                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open(os.path.join(path, filename), 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                        logger.debug(
                            f"Image Downloaded Sucessfuly - {filename}")
                else:
                    logger.critical('Image Couldn\'t be retreived')
    else:
        logger.warning("Operation Cancelled by the User.")
    showinfo("Success", "All Downloaded successfully.")


link = Entry(root, width=50)
link.pack(pady=30)
file = Button(root, text='Select a File.', command=selectFile)
file.pack(pady=2)
downloader = Button(root, text="Download", command=download,
                    width=20, bg='#E06F57')

downloader.pack(pady=5)
if __name__ == '__main__':
    root.mainloop()
