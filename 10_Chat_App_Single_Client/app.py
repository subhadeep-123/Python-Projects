import pymongo
from tkinter import *
from tkinter.messagebox import *


root = Tk()
root.geometry("700x500")
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
    result = col.insert_one(data).inserted_id
    print(f"Data Inserted for Object ID - {result}")


def log_in():
    if col.count_documents({'Username': username.get(), 'Password': password.get()}) > 0:
        showinfo('Welcome', f"You are logged in now - {username.get()}")


userlabel = Label(root, text='UserName:- ').grid(row=0,
                                                 column=0, pady=50)
username = Entry(root, width=50)
username.grid(row=0, column=1, pady=50)

password = Label(root, text='Password:- ').grid(row=1,
                                                column=0, pady=20)
password = Entry(root, width=50)
password.grid(row=1, column=1, pady=20)

Sign_Up = Button(root, text='Sign Up', command=sign_up)
Sign_Up.grid(row=2, column=0, padx=20)
Log_In = Button(root, text='Log In', command=log_in)
Log_In.grid(row=2, column=1)


if __name__ == '__main__':
    root.mainloop()
