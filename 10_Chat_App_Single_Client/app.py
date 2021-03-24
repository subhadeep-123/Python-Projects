import pymongo
from tkinter import *
from tkinter.messagebox import *


root = Tk()
root.geometry("700x500+10+20")
root.title("Socket Chap App")
root.iconbitmap('assets\logo.ico')

client = pymongo.MongoClient()
db = client.account_data
col = db.records


def sign_up():
    data = {
        'Username': username.get(),
        'Password': password.get()
    }
    if not col.count_documents(data) > 1:
        result = col.insert_one(data).inserted_id
        print(f"Data Inserted for Object ID - {result}")
        showinfo('Sign Up Successful',
                 f"You have now signed up in chatly - {username.get()}")
    else:
        showerror("SignUp Error", "Account Alreay Exists")


def newWindow():
    top = Toplevel()
    top.title("Chat Window")
    root.iconbitmap('assets\logo.ico')
    toshow = Label()
    Button(top, text="Close Window", compound=top.destroy).pack()


def log_in():
    if col.count_documents({'Username': username.get(), 'Password': password.get()}) > 0:
        showinfo('Welcome', f"You are logged in now - {username.get()}")
        # root.destroy()
        newWindow()
    else:
        showerror("Log In Error", "Account Does Not Exist.")


userlabel = Label(root, text='UserName:- ').place(x=150, y=100)

username = Entry(root, width=50)
username.place(x=240, y=100)

password = Label(root, text='Password:- ').place(x=150, y=150)

password = Entry(root, width=50)
password.place(x=240, y=150)

Sign_Up = Button(root, text='Sign Up', command=sign_up).place(x=320, y=200)
Log_In = Button(root, text='Log In', command=log_in).place(x=260, y=200)


if __name__ == '__main__':
    root.mainloop()
