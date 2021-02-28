import os
import ssl
import smtplib
import getpass
from tkinter import *
from email import encoders
from tkinter import filedialog
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

root = Tk()
root.title('Email Automation')
root.iconbitmap('assets\logo.ico')
root.geometry("450x450")

PORT = 465
SERVER = 'smtp.gmail.com'
FILE = 'index.html'
CONTEXT = ssl.create_default_context()

filename = None
image_filename = None


def select_image():
    global image_filename
    username = getpass.getuser()
    image_filename = filedialog.askopenfilename(title="Select an Image", filetype=(
        ("PNG", "*.png"),
        ("JPEG", "*.jpg"),
        ("JPEG", "*.jpeg")),
        initialdir=f"C:/Users/{username}/Desktop"
    )
    image_btn = Button(root, text=f"Selected - {os.path.split(image_filename)[1]}",
                       command=select_image).grid(row=5, column=2, sticky='W')


def select_file():
    global filename
    username = getpass.getuser()
    filename = filedialog.askopenfilename(title="Select an Image", filetype=(
        ("All File", "*.*"),
    ),
        initialdir=f"C:/Users/{username}/Desktop"
    )
    file_btn = Button(root, text=f"Selected - {os.path.split(filename)[1]}",
                      command=select_file).grid(row=6, column=2, sticky='W')


def clrscr():
    uname.grid_forget()
    passwd.grid_forget()
    to.grid_forget()
    subject.grid_forget()
    message_text.grid_forget()


def sendMail():
    message = MIMEMultipart()
    message["From"] = uname.get()
    message["To"] = to.get()
    message["Subject"] = subject.get()
    # message["Bcc"] = receiver_email
    message.attach(MIMEText(message_text.get(1.0, END), 'plain'))

    file = None

    if image_filename != None:
        file = image_filename
    if filename != None:
        file = filename

    if file != None:
        with open(file, "rb") as attatchment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attatchment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {file}",
        )

        message.attach(part)

    text = message.as_string()

    try:
        with smtplib.SMTP_SSL(SERVER, PORT, context=CONTEXT) as server:
            server.login(uname.get(), passwd.get())
            server.sendmail(uname.get(), to.get(), text)
            server.quit()
    except Exception as err:
        print(err)

    clrscr()


# username
uname_label = Label(root, text="Username: ").grid(row=0, column=0)
uname = Entry(root, width=30)
uname.grid(row=0, column=2, sticky=W)
uname.insert(0, "Enter Your Username")

# password
passwd_label = Label(root, text="Password: ").grid(row=1, column=0)
passwd = Entry(root, width=30)
passwd.grid(row=1, column=2, sticky=W)
passwd.insert(0, "Enter Your Password")

# to
to_label = Label(root, text="To: ").grid(row=2, column=0)
to = Entry(root, width=30)
to.grid(row=2, column=2, sticky=W)
to.insert(0, "Enter Recivers Email")

# subject
subject_label = Label(root, text="Subject: ").grid(row=3, column=0)
subject = Entry(root, width=30)
subject.grid(row=3, column=2, sticky=W)
subject.insert(0, "Enter Your Subject")

# message
message_label = Label(root, text="Message: ").grid(row=4, column=0)
message_text = Text(root, width=30, height=15)
message_text.grid(row=4, column=2)

# image
image_label = Label(root, text="Image: ").grid(row=5, column=0)
image_btn = Button(root, text='Select Image',
                   command=select_image).grid(row=5, column=2, sticky='W')

# doc/pdf/and other format file
file_label = Label(root, text="File: ").grid(row=6, column=0)
file_btn = Button(root, text='Select File',
                  command=select_file).grid(row=6, column=2, sticky='W')

# sendmail
sendmail_btn = Button(root, text='SendMail',
                      command=sendMail).grid(row=8, column=2)

if __name__ == '__main__':
    root.mainloop()
