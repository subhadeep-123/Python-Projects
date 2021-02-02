from tkinter import *

root = Tk()
root.title("Basic Calculator")

a = Entry(root, width=35, borderwidth=5)
a.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(num):
    current = a.get()
    a.delete(0, END)
    a.insert(0, str(current) + str(num))


def btn_clear():
    a.delete(0, END)


def btn_add():
    fnum = a.get()
    global f_num
    global math
    math = "addition"
    f_num = int(fnum)
    a.delete(0, END)


def btn_sub():
    fnum = a.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(fnum)
    a.delete(0, END)


def btn_mult():
    fnum = a.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(fnum)
    a.delete(0, END)


def btn_div():
    fnum = a.get()
    global f_num
    global math
    math = "division"
    f_num = int(fnum)
    a.delete(0, END)


def btn_equal():
    snum = a.get()
    a.delete(0, END)
    if math == 'addition':
        a.insert(0, f_num+int(snum))
    if math == 'substraction':
        a.insert(0, f_num-int(snum))
    if math == 'multiplication':
        a.insert(0, f_num*int(snum))
    if math == 'division':
        a.insert(0, f_num/int(snum))


        # Definig Buttons
btn_1 = Button(root, text="1", padx=40, pady=20,
               command=lambda: button_click(1))
btn_2 = Button(root, text="2", padx=40, pady=20,
               command=lambda: button_click(2))
btn_3 = Button(root, text="3", padx=40, pady=20,
               command=lambda: button_click(3))
btn_4 = Button(root, text="4", padx=40, pady=20,
               command=lambda: button_click(4))
btn_5 = Button(root, text="5", padx=40, pady=20,
               command=lambda: button_click(5))
btn_6 = Button(root, text="6", padx=40, pady=20,
               command=lambda: button_click(6))
btn_7 = Button(root, text="7", padx=40, pady=20,
               command=lambda: button_click(7))
btn_8 = Button(root, text="8", padx=40, pady=20,
               command=lambda: button_click(8))
btn_9 = Button(root, text="9", padx=40, pady=20,
               command=lambda: button_click(9))
btn_0 = Button(root, text="0", padx=40, pady=20,
               command=lambda: button_click(0))
button_equal = Button(root, text="=", padx=91, pady=20,
                      command=btn_equal)
button_clear = Button(root, text="Clear", padx=79,
                      pady=20, command=lambda: btn_clear())

button_add = Button(root, text="+", padx=39, pady=20,
                    command=btn_add)
button_sub = Button(root, text="-", padx=41, pady=20,
                    command=btn_sub)
button_mult = Button(root, text="*", padx=40, pady=20,
                     command=btn_mult)
button_div = Button(root, text="/", padx=42, pady=20,
                    command=btn_div)

# Put Buttons on the screen
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_sub.grid(row=6, column=0)
button_mult.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()
