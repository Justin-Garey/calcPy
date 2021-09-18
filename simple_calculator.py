## Import everything related to tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
import math

## Root widget
root = Tk()
root.geometry("270x260")
root.minsize(width=270, height=260)
root.maxsize(width=540, height=520)


## Change root color
root.configure(bg='gray')

## Change font size
##font_style = font.Font(family="Lucida Fax", size=15)

## Title this simple calculator
root.title("Simple Calculator")

## Icon
root.iconbitmap('images/icon2.ico')

## Create a frame for the calculator
myFrame = LabelFrame(root, padx=20, pady=20, bg="gray")

## Define the entry box
e = Entry(myFrame, width=20) #, font=font_style)

## Define global variables
global old_value
global current_value
global new_value
global last_op
global current_op
global is_decimal
old_value = 0
current_value = 0
new_value = 0
last_op = ''
current_op = ''
is_decimal = False

## Variables for checking is the equals button was pressed
global equals_pressed
equals_pressed = 0

## Checks if a number is an integer or float
def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

## Function for resetting equals counter
def equals_pressed_checker():
    global equals_pressed
    global last_op
    global current_op
    if equals_pressed > 0:
        last_op = ''
        current_op = ''
    equals_pressed = 0

## Define function for concatenating the string
def add_value(number):
    global is_decimal
    equals_pressed_checker()
    current_number = e.get()
    e.delete(0, END)
    if number == '.':
        is_decimal = True
    if current_number != '0':
        number = current_number + number
    e.insert(0, number)

## Function to create the first value
def value_initializer():
    equals_pressed_checker()
    global old_value
    global current_value
    global new_value
    global last_op
    global current_op
    current_value = float(e.get())
    if last_op == '*':
        new_value = old_value * current_value
    elif last_op == '/':
        new_value = old_value / current_value
    elif last_op == '-':
        new_value = old_value - current_value
    elif last_op == '+':
        new_value = old_value + current_value
    else:
        new_value = current_value
    last_op = current_op
    old_value = new_value

## Define function for multiplying
def multiply():
    equals_pressed_checker()
    global current_op
    current_op = '*'
    value_initializer()
    e.insert(END, current_op)

## Define function for dividing
def divide():
    equals_pressed_checker()
    global current_op
    current_op = '/'
    value_initializer()
    e.insert(END, current_op)

## Define function for subtracting
def subtract():
    equals_pressed_checker()
    global current_op
    if (e.get() == '0' or current_op != ''):
        add_value('-')
    else:
        current_op = '-'
        value_initializer()
        e.insert(END, current_op)

## Define function for adding
def add():
    equals_pressed_checker()
    global current_op
    current_op = '+'
    value_initializer()
    e.insert(END, current_op)

## Define function for clearing the entry box
def clear():
    equals_pressed_checker()
    global old_value
    global current_value
    global new_value
    global last_op
    global current_op
    global is_decimal
    old_value = 0
    current_value = 0
    new_value = 0
    last_op = ''
    current_op = ''
    is_decimal = False
    e.delete(0,END)
    e.insert(0, new_value)

## Define function for solving
def equals():
    global equals_pressed
    global old_value
    global current_value
    global new_value
    global last_op
    global saved_op
    global is_decimal
    if equals_pressed == 0:
        temp = e.get()
        if (current_op == '*'):
            temp = temp[temp.index('*')+1:]
        elif (current_op == '/'):
            temp = temp[temp.index('/')+1:]
        elif (current_op == '+'):
            temp = temp[temp.index('+')+1:]
        elif (current_op == '-'):
            if old_value < 0:
                if is_decimal:
                    temp = temp.replace(str(old_value), '')
                else:
                    temp = temp.replace(str(int(old_value)), '')
            temp = temp[temp.index('-')+1:]
        else:
            pass
        current_value = float(temp)
        if last_op == '*':
            new_value = old_value * current_value
        elif last_op == '/':
            new_value = old_value / current_value
        elif last_op == '-':
            new_value = old_value - current_value
        elif last_op == '+':
            new_value = old_value + current_value
        saved_op = last_op
        last_op = '='
    elif (equals_pressed == 1):
        last_op = '='
        if saved_op == '*':
            new_value = old_value * current_value
        elif saved_op == '/':
            new_value = old_value / current_value
        elif saved_op == '-':
            new_value = old_value - current_value
        elif saved_op == '+':
            new_value = old_value + current_value
    else:
        last_op = '='
        if saved_op == '*':
            new_value = old_value * current_value
        elif saved_op == '/':
            new_value = old_value / current_value
        elif saved_op == '-':
            new_value = old_value - current_value
        elif saved_op == '+':
            new_value = old_value + current_value
    if (abs(new_value) < 0.0001 and abs(new_value) > 0):
        clear()
    elif (abs(new_value) > 2000000000):
        clear()
    else:
        old_value = new_value
        e.delete(0,END)
        if (is_decimal == False and is_integer_num(new_value)) or is_integer_num(new_value):
            new_value = int(new_value)
        if (is_decimal == True and not is_integer_num(new_value)) or not is_integer_num(new_value):
            is_decimal = True
            new_value = str(new_value)
            new_value = new_value[:new_value.index('.')+6]
        e.insert(0, new_value)
        equals_pressed += 1

## load images
img_9 = ImageTk.PhotoImage(Image.open("images/9.png"))
img_8 = ImageTk.PhotoImage(Image.open("images/8.png"))
img_7 = ImageTk.PhotoImage(Image.open("images/7.png"))
img_6 = ImageTk.PhotoImage(Image.open("images/6.png"))
img_5 = ImageTk.PhotoImage(Image.open("images/5.png"))
img_4 = ImageTk.PhotoImage(Image.open("images/4.png"))
img_3 = ImageTk.PhotoImage(Image.open("images/3.png"))
img_2 = ImageTk.PhotoImage(Image.open("images/2.png"))
img_1 = ImageTk.PhotoImage(Image.open("images/1.png"))
img_0 = ImageTk.PhotoImage(Image.open("images/0.png"))
img_multiply = ImageTk.PhotoImage(Image.open("images/multiplication.png"))
img_divide = ImageTk.PhotoImage(Image.open("images/division.png"))
img_plus = ImageTk.PhotoImage(Image.open("images/plus.png"))
img_minus = ImageTk.PhotoImage(Image.open("images/minus.png"))
img_dec = ImageTk.PhotoImage(Image.open("images/decimal.png"))
img_clear = ImageTk.PhotoImage(Image.open("images/clear.png"))
img_equals = ImageTk.PhotoImage(Image.open("images/equal.png"))

## Define the buttons
button_7 = Button(myFrame, image = img_7, height=40, width=40, bg="darkgray", activebackground="gray", command=lambda: add_value('7'))
button_8 = Button(myFrame, image = img_8, height=40, width=40, bg="darkgray", activebackground="gray",  command=lambda: add_value('8')) 
button_9 = Button(myFrame, image = img_9, height=40, width=40, bg="darkgray", activebackground="gray",  command=lambda: add_value('9')) 
button_star = Button(myFrame, image = img_multiply, height=40, width=40, bg="darkgray", activebackground="gray",  command=multiply)

button_4 = Button(myFrame, image = img_4, height=40, width=40, bg="darkgray", activebackground="gray",  command=lambda: add_value('4'))
button_5 = Button(myFrame, image = img_5, height=40, width=40, bg="darkgray", activebackground="gray",  command=lambda: add_value('5')) 
button_6 = Button(myFrame, image = img_6, height=40, width=40, bg="darkgray", activebackground="gray",  command=lambda: add_value('6')) 
button_slash = Button(myFrame, image = img_divide, height=40, width=40, bg="darkgray", activebackground="gray",  command=divide) 

button_1 = Button(myFrame, image = img_1, height=40, width=40, bg="darkgray", activebackground="gray",  command=lambda: add_value('1'))
button_2 = Button(myFrame, image = img_2, height=40, width=40, bg="darkgray", activebackground="gray",  command=lambda: add_value('2')) 
button_3 = Button(myFrame, image = img_3, height=40, width=40, bg="darkgray",  activebackground="gray", command=lambda: add_value('3')) 
button_minus = Button(myFrame, image = img_minus, height=40, width=40, bg="darkgray", activebackground="gray",  command=subtract) 

button_0 = Button(myFrame, image = img_0, height=40, width=40, bg="darkgray", activebackground="gray",  command=lambda: add_value('0'))
button_dec = Button(myFrame, image = img_dec, height=40, width=40, bg="darkgray",  activebackground="gray", command=lambda: add_value('.')) 
button_clear = Button(myFrame, image = img_clear, height=40, width=40, bg="darkgray", activebackground="gray",  command=clear) 
button_plus = Button(myFrame, image = img_plus, height=40, width=40, bg="darkgray", activebackground="gray",  command=add) 

button_equal = Button(myFrame, image = img_equals, height=178, width=40, bg="darkgray", activebackground="gray",  command=equals)
## Display entry box
e.grid(row = 0, column=0, columnspan=5, pady=(0,10), sticky=E+W+N+S) # , ipady=10, ipadx=50
e.insert(0, '0')

## Display buttons
button_7.grid(row=1, column=0, sticky=E+W+N+S)
button_8.grid(row=1, column=1, sticky=E+W+N+S)
button_9.grid(row=1, column=2, sticky=E+W+N+S)
button_star.grid(row=1, column=3, sticky=E+W+N+S)

button_4.grid(row=2, column=0, sticky=E+W+N+S)
button_5.grid(row=2, column=1, sticky=E+W+N+S)
button_6.grid(row=2, column=2, sticky=E+W+N+S)
button_slash.grid(row=2, column=3, sticky=E+W+N+S)

button_1.grid(row=3, column=0, sticky=E+W+N+S)
button_2.grid(row=3, column=1, sticky=E+W+N+S)
button_3.grid(row=3, column=2, sticky=E+W+N+S)
button_minus.grid(row=3, column=3, sticky=E+W+N+S)

button_0.grid(row=4, column=0, sticky=E+W+N+S)
button_dec.grid(row=4, column=1, sticky=E+W+N+S)
button_clear.grid(row=4, column=2, sticky=E+W+N+S)
button_plus.grid(row=4, column=3, sticky=E+W+N+S)

button_equal.grid(row=1, column=4, rowspan=4, sticky=E+W+N+S)

## Pack in the frame
myFrame.grid(row=0, column=0, sticky=E+W+N+S)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

myFrame.rowconfigure(0, weight=1)
myFrame.columnconfigure(0, weight=1)
myFrame.rowconfigure(1, weight=1)
myFrame.columnconfigure(1, weight=1)
myFrame.rowconfigure(2, weight=1)
myFrame.columnconfigure(2, weight=1)
myFrame.rowconfigure(3, weight=1)
myFrame.columnconfigure(3, weight=1)
myFrame.rowconfigure(4, weight=1)
myFrame.columnconfigure(4, weight=1)

## Resize the text dynamically
def resize(x):
    size = x.width / 13.5
    e.config(font=("Lucida Fax", int(size)))

root.bind('<Configure>', resize)


e.bind("<Key>", lambda e: "break")  # lambda e: "break" will disabel keyboard input
e.bind('<Control-v>', lambda e: 'break') #disable paste

## This loops the program as a window
root.mainloop()