from os import pipe
from tkinter import *
from tkinter.messagebox import showerror

root = Tk()
root.title("Unit Converter")
root.geometry("510x400")
root.iconbitmap('assets\icon.ico')

options = ["Kilometer", "Meter", "Centimeter", "Millimeter", "Micrometers",
           "Nanometer", "Mile", "Yard", "Foot", "Inch", "Nautical Mile"]


def show(val):
    # show calculated results
    rightTo = Entry(root)
    rightTo.place(x=380, y=107)
    rightTo.insert(END, val)


def convert():
    val = int(leftTo.get())
    leftch = left.get()
    rightch = right.get()
    if leftch == 'Kilometer':
        if rightch == 'Kilometer':
            show(val)
        elif rightch == 'Meter':
            val *= 1000
            show(val)
        elif rightch == 'Centimeter':
            val *= 100000
            show(val)
        elif rightch == 'Millimeter':
            val *= 1000000
            show(val)
        elif rightch == 'Micrometers':
            val *= 1000000000
            show(val)
        elif rightch == 'Nanometer':
            val *= 1000000000000
            show(val)
        elif rightch == 'Mile':
            val *= 0.621371
            show(val)
        elif rightch == 'Yard':
            val *= 1093.61
            show(val)
        elif rightch == 'Foot':
            val *= 3280.84
            show(val)
        elif rightch == 'Inch':
            val *= 39370.1
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 0.539957
            show(val)
        else:
            print('Does Not Exist.')
    elif leftch == 'Meter':
        if rightch == 'Kilometer':
            val *= 0.001
            show(val)
        elif rightch == 'Meter':
            show(val)
        elif rightch == 'Centimeter':
            val *= 100
            show(val)
        elif rightch == 'Millimeter':
            val *= 1000
            show(val)
        elif rightch == 'Micrometers':
            val *= 1000000
            show(val)
        elif rightch == 'Nanometer':
            val *= 1000000000
            show(val)
        elif rightch == 'Mile':
            val *= 0.000621371
            show(val)
        elif rightch == 'Yard':
            val *= 1.09361
            show(val)
        elif rightch == 'Foot':
            val *= 3.28084
            show(val)
        elif rightch == 'Inch':
            val *= 39.3701
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 0.000539957
            show(val)
        else:
            print('Does Not Exist.')
    elif leftch == 'Centimeter':
        if rightch == 'Kilometer':
            val *= 0.00001
            show(val)
        elif rightch == 'Meter':
            val *= 0.01
            show(val)
        elif rightch == 'Centimeter':
            show(val)
        elif rightch == 'Millimeter':
            val *= 10
            show(val)
        elif rightch == 'Micrometers':
            val *= 10000
            show(val)
        elif rightch == 'Nanometer':
            val *= 10000000
            show(val)
        elif rightch == 'Mile':
            val *= 0.0000062137
            show(val)
        elif rightch == 'Yard':
            val *= 0.0109361
            show(val)
        elif rightch == 'Foot':
            val *= 0.0328084
            show(val)
        elif rightch == 'Inch':
            val *= 0.393701
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 0.00000539957
            show(val)
        else:
            print('Does Not Exist.')
    elif leftch == 'Millimeter':
        if rightch == 'Kilometer':
            val *= 0.000001
            show(val)
        elif rightch == 'Meter':
            val *= 0.001
            show(val)
        elif rightch == 'Centimeter':
            val *= 0.1
            show(val)
        elif rightch == 'Millimeter':
            val *= 1
            show(val)
        elif rightch == 'Micrometers':
            val *= 1000
            show(val)
        elif rightch == 'Nanometer':
            val *= 1000000
            show(val)
        elif rightch == 'Mile':
            val *= 0.0000000621371
            show(val)
        elif rightch == 'Yard':
            val *= 0.00109361
            show(val)
        elif rightch == 'Foot':
            val *= 0.00328084
            show(val)
        elif rightch == 'Inch':
            val *= 0.0393701
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 0.000000539957
            show(val)
        else:
            print('Does Not Exist.')
    elif leftch == 'Micrometers':
        if rightch == 'Kilometer':
            val *= 0.000000001
            show(val)
        elif rightch == 'Meter':
            val *= 0.000001
            show(val)
        elif rightch == 'Centimeter':
            val *= 0.0001
            show(val)
        elif rightch == 'Millimeter':
            val *= 0.001
            show(val)
        elif rightch == 'Micrometers':
            val *= 1
            show(val)
        elif rightch == 'Nanometer':
            val *= 1000
            show(val)
        elif rightch == 'Mile':
            val *= 0.000000000621371
            show(val)
        elif rightch == 'Yard':
            val *= 0.00000109361
            show(val)
        elif rightch == 'Foot':
            val *= 0.00000328084
            show(val)
        elif rightch == 'Inch':
            val *= 0.0000393701
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 0.000000000539957
            show(val)
        else:
            print('Does Not Exist.')
    elif leftch == 'Nanometer':
        if rightch == 'Kilometer':
            val *= 0.000000000001
            show(val)
        elif rightch == 'Meter':
            val *= 0.000000001
            show(val)
        elif rightch == 'Centimeter':
            val *= 0.0000001
            show(val)
        elif rightch == 'Millimeter':
            val *= 0.000001
            show(val)
        elif rightch == 'Micrometers':
            val *= 0.001
            show(val)
        elif rightch == 'Nanometer':
            val *= 1
            show(val)
        elif rightch == 'Mile':
            val *= 0.000000000000621371
            show(val)
        elif rightch == 'Yard':
            val *= 0.00000000109361
            show(val)
        elif rightch == 'Foot':
            val *= 0.00000328084
            show(val)
        elif rightch == 'Inch':
            val *= 0.00000000393701
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 0.000000000000539957
            show(val)
        else:
            print('Does Not Exist.')
    elif leftch == 'Mile':
        if rightch == 'Kilometer':
            val *= 1.60934
            show(val)
        elif rightch == 'Meter':
            val *= 1609.34
            show(val)
        elif rightch == 'Centimeter':
            val *= 160934
            show(val)
        elif rightch == 'Millimeter':
            val *= 1609000
            show(val)
        elif rightch == 'Micrometers':
            val *= 1609000000
            show(val)
        elif rightch == 'Nanometer':
            val *= 1609000000000
            show(val)
        elif rightch == 'Mile':
            val *= 1
            show(val)
        elif rightch == 'Yard':
            val *= 1760
            show(val)
        elif rightch == 'Foot':
            val *= 5280
            show(val)
        elif rightch == 'Inch':
            val *= 63360
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 0.868976
            show(val)
        else:
            print('Does Not Exist.')
    elif leftch == 'Yard':
        if rightch == 'Kilometer':
            val *= 0.0009144
            show(val)
        elif rightch == 'Meter':
            val *= 0.9144
            show(val)
        elif rightch == 'Centimeter':
            val *= 91.44
            show(val)
        elif rightch == 'Millimeter':
            val *= 914.4
            show(val)
        elif rightch == 'Micrometers':
            val *= 914400
            show(val)
        elif rightch == 'Nanometer':
            val *= 9.14400000
            show(val)
        elif rightch == 'Mile':
            val *= 0.000568182
            show(val)
        elif rightch == 'Yard':
            val *= 1
            show(val)
        elif rightch == 'Foot':
            val *= 3
            show(val)
        elif rightch == 'Inch':
            val *= 36
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 0.000493737
            show(val)
        else:
            print('Does Not Exist.')
    elif leftch == 'Foot':
        if rightch == 'Kilometer':
            val *= 0.0003048
            show(val)
        elif rightch == 'Meter':
            val *= 0.3048
            show(val)
        elif rightch == 'Centimeter':
            val *= 30.48
            show(val)
        elif rightch == 'Millimeter':
            val *= 30.48
            show(val)
        elif rightch == 'Micrometers':
            val *= 304.8
            show(val)
        elif rightch == 'Nanometer':
            val *= 3.04800000
            show(val)
        elif rightch == 'Mile':
            val *= 0.000189394
            show(val)
        elif rightch == 'Yard':
            val *= 0.333333
            show(val)
        elif rightch == 'Foot':
            val *= 1
            show(val)
        elif rightch == 'Inch':
            val *= 12
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 0.000164579
            show(val)
        else:
            print('Does Not Exist.')
    elif leftch == 'Inch':
        if rightch == 'Kilometer':
            val *= 0.0000254
            show(val)
        elif rightch == 'Meter':
            val *= 0.0254
            show(val)
        elif rightch == 'Centimeter':
            val *= 2.54
            show(val)
        elif rightch == 'Millimeter':
            val *= 25.4
            show(val)
        elif rightch == 'Micrometers':
            val *= 25400
            show(val)
        elif rightch == 'Nanometer':
            val *= 2.5400000
            show(val)
        elif rightch == 'Mile':
            val *= 0.000015783
            show(val)
        elif rightch == 'Yard':
            val *= 0.0277778
            show(val)
        elif rightch == 'Foot':
            val *= 0.0833333
            show(val)
        elif rightch == 'Inch':
            val *= 1
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 0.0000137149
            show(val)
        else:
            print('Does Not Exist.')
    elif leftch == 'Nautical Mile':
        if rightch == 'Kilometer':
            val *= 1.852
            show(val)
        elif rightch == 'Meter':
            val *= 1852
            show(val)
        elif rightch == 'Centimeter':
            val *= 185200
            show(val)
        elif rightch == 'Millimeter':
            val *= 1852000
            show(val)
        elif rightch == 'Micrometers':
            val *= 1852000000
            show(val)
        elif rightch == 'Nanometer':
            val *= 1852000000000
            show(val)
        elif rightch == 'Mile':
            val *= 1.15078
            show(val)
        elif rightch == 'Yard':
            val *= 2025.37
            show(val)
        elif rightch == 'Foot':
            val *= 6076.12
            show(val)
        elif rightch == 'Inch':
            val *= 72913.4
            show(val)
        elif rightch == 'Nautical Mile':
            val *= 1
            show(val)
        else:
            print('Does Not Exist.')
    else:
        print('Does Not Exist.')


# Left Options
left = StringVar()
left.set("Options")
leftDrop = OptionMenu(root, left, *options)
leftDrop.place(x=5, y=100)

# left To
leftTo = Entry(root)
leftTo.place(x=125, y=107)

# Convert Button
convert = Button(root, text="Convert",
                 command=convert)
convert.place(x=220, y=140)

# Right Options
right = StringVar()
right.set("Options")
rightDrop = OptionMenu(root, right, *options)
rightDrop.place(x=260, y=100)

# Right From
rightTo = Entry(root, state=DISABLED)
rightTo.place(x=380, y=107)

if __name__ == '__main__':
    root.mainloop()
