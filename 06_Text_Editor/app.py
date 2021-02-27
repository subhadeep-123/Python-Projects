from tkinter import *
from tkinter import filedialog
root = Tk()
root.iconbitmap('assets\logo.ico')
root.title('MatrixPad')
root.rowconfigure(0, minsize=500, weight=1)
root.columnconfigure(1, minsize=900, weight=1)


def save_function():
    """
    Save a file after editing
    """
    filepath = filedialog.asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"),
                   ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_space.get(1.0, END)
        output_file.write(text)
    root.title(f"MatrixPad - {filepath}")


def open_function():
    """
    Open a file for editing
    """
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", '*.txt'),
                                                     ("All Files", "*.*")]
                                          )
    if not filepath:
        return
    text_space.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_space.insert(END, text)
    root.title(f"MatrixPad - {filepath}")


text_space = Text(root)
text_space.grid(row=0, column=1, sticky='nsew')

fr_button = Frame(root)
fr_button.grid(row=0, column=0, sticky='ns')

save_btn = Button(fr_button, text='SaveAs', command=save_function)
save_btn.grid(row=0, column=0, sticky='ew', padx=5)

open_btn = Button(fr_button, text='Open', command=open_function)
open_btn.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

root.mainloop()
