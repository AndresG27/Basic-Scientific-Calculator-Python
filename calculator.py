from tkinter import *
from tkinter.messagebox import *
import numpy as np


#Creating the main program
root = Tk()
root.title("Calculator")
root.resizable(0, 0) #this line allows (or not) the user to change de window size, in this case it doesn't
                     #each atribute indicates what axis can the user modify
root.config(bg="lightgrey")
photo = PhotoImage(file = 'calc.png')
root.wm_iconphoto(True, photo)
#creating the functions for the calculations
def data_entry(value):
  previous = entry.get()
  entry.delete(0, END)
  entry.insert(0, str(previous) + str(value))  

def erase_data():
    entry.delete(0, END)
    
def equal():
    global num_2
    global num_3
    num_2 = entry.get()
    num_2 = float(num_2)
    if operation == "+":
        num_3 = num_1 + num_2
        showinfo("Result", 
                 f"The result of {num_1} + {num_2} is: {num_3}")
    elif operation == "-":
        num_3 = num_1 - num_2
        showinfo("Result",
                 f"The result of {num_1} - {num_2} is: {num_3}")
    elif operation == "x":
        num_3 = num_1 * num_2
        num_3 = round(num_3, 4)
        showinfo("Result",
                 f"The result of {num_1} x {num_2} is: {num_3}")
    elif operation == "/":
        if num_2 != 0:
            num_3 = num_1 / num_2
            num_3 = round(num_3, 4)
            showinfo("Result",
                     f"The result of {num_1} / {num_2} is: {num_3}")
        else:
            showerror("Error",
                      "You cannot divide by 0")
    elif operation == "%":
        num_3 = num_1 * (num_2/100)
        showinfo("Result",
                 f"The {num_2}% of {num_1} is {num_3}")        
    elif operation == "^":
        if num_1 == 0 and num_2 == 0:
            showerror("Error",
                      "Indetermination")
        else:
            num_3  = num_1 ** num_2
            showinfo("Result",
                    f"{num_1} to the power of {num_2} is equal to {num_3}")
    elif operation == "yroot":
        if num_2 != 0:
            num_3 = num_1 ** (1/num_2)
            num_3 = round(num_3, 5)
            showinfo("Result", 
                     f"The {num_2} of {num_1} is equal to {num_3}")
        else:
            showerror("Error",
                      "Your root subindex cannot be 0")

    entry.delete(0, END)
    
def add():
    global num_1
    global operation
    operation = "+"
    num_1 = entry.get()
    num_1 = float(num_1)
    entry.delete(0, END)
    
def sub():
    global operation
    global num_1 
    operation = "-"    
    num_1 = entry.get()
    num_1 = float(num_1)
    entry.delete(0, END)

def mult():
    global num_1
    global operation
    operation = "x"
    num_1 = entry.get()
    num_1 = float(num_1)
    entry.delete(0, END)

def div():
    global num_1
    global operation
    operation = "/"
    num_1 = entry.get()
    num_1 = float(num_1)
    entry.delete(0, END)

def sin():
    global num_1
    global num_2
    num_1 = entry.get()
    num_1 = float(num_1)
    entry.delete(0, END)
    num_2 = np.sin(num_1)
    num_2 = round(num_2, 6)
    entry.delete(0, END)
    showinfo("Result",
             f"The sin of {num_1} in radians is {num_2}")
def cos():
    global num_1
    global num_2
    num_1 = entry.get()
    num_1 = float(num_1)
    entry.delete(0, END)
    num_2 = np.cos(num_1)
    num_2 = round(num_2, 6)
    entry.delete(0, END)
    showinfo("Result",
             f"The cos of {num_1} in radians is {num_2}")

def square():
    global num_1
    global num_2
    num_1 = entry.get()
    num_1 = float(num_1)
    num_2 = num_1**2
    entry.delete(0, END)
    showinfo("Result", 
             f"{num_1} squared is equal to: {num_2}")
def square_root():
    global num_1
    global num_2
    num_1 = entry.get()
    num_1 = float(num_1)
    num_2 = num_1**(1/2)
    num_2 = round(num_2, 4)
    entry.delete(0, END)
    showinfo("Result", 
             f"The square root of {num_1} is equal to: {num_2}")
def percentage():
    global num_1
    global operation
    num_1 = entry.get()
    num_1 = float(num_1)
    entry.delete(0, END)
    operation = "%"
def power():
    global num_1
    global operation
    num_1 = entry.get()
    num_1 = float(num_1)
    entry.delete(0, END)
    operation = "^"
def y_root():
    global num_1
    global operation
    operation = "yroot"
    num_1 = entry.get()
    num_1 = float(num_1)
    entry.delete(0, END)

#Creating the buttons
entry = Entry(root, 
              width=25, 
              borderwidth=0,
              font=("arial", 18, 'bold'))
entry.grid(row=0, columnspan=4, padx=3, pady=3)

sin_button = Button(root,
                    text="Sin",
                    width=10,
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : sin()).grid(row=1, column=0, padx=3, pady=3)

cos_button = Button(root,
                    text="Cos",
                    width=10,
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : cos()).grid(row=1, column=1, padx=3, pady=3)
square_button = Button(root,
                    text="x²",
                    width=10,
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : square()).grid(row=1, column=2, padx=3, pady=3)

power_button = Button(root,
                    text="x^y",
                    width=10,
                    borderwidth=0,
                    cursor="hand2",
                    command= lambda : power()).grid(row=1, column=3, padx=3, pady=3)

sqr_root_button = Button(root,
                    text="√",
                    width=10,
                    borderwidth=0,
                    cursor="hand2",
                    command= lambda : square_root()).grid(row=2, column=0, padx=3, pady=3)

y_root_button = Button(root,
                    text="y√",
                    width=10,
                    borderwidth=0,
                    cursor="hand2",
                    command= lambda : y_root()).grid(row=2, column=1, padx=3, pady=3)

percentage_button = Button(root,
                    text="%",
                    width=10,
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : percentage()).grid(row=2, column=2, padx=3, pady=3)

delete_button = Button(root,
                    text="Delete",
                    width=10,
                    borderwidth=0,
                    cursor="hand2",
                    command= lambda : erase_data()).grid(row=2, column=3, padx=3, pady=3)

button_7 = Button(root,
                text="7",
                width=10,
                borderwidth=0,
                cursor="hand2",
                command=lambda : data_entry(7)).grid(row=3, column=0, padx=3, pady=3)

button_8 = Button(root,
                text="8",
                width=10,
                borderwidth=0,
                cursor="hand2",
                command=lambda : data_entry(8)).grid(row=3, column=1, padx=3, pady=3)

button_9 = Button(root,
                text="9",
                width=10,
                borderwidth=0,
                cursor="hand2",
                command=lambda : data_entry(9)).grid(row=3, column=2, padx=3, pady=3)

addition_button = Button(root,
                    text="+",
                    width=10,
                    borderwidth=0,
                    cursor="hand2",
                    command= lambda : add()).grid(row=3, column=3, padx=3, pady=3)

button_4 = Button(root,
                text="4",
                width=10,
                borderwidth=0,
                cursor="hand2",
                command=lambda : data_entry(4)).grid(row=4, column=0, padx=3, pady=3)

button_5 = Button(root,
                text="5",
                width=10,
                borderwidth=0,
                cursor="hand2",
                command=lambda : data_entry(5)).grid(row=4, column=1, padx=3, pady=3)

button_6 = Button(root,
                text="6",
                width=10,
                borderwidth=0,
                cursor="hand2",
                command=lambda : data_entry(6)).grid(row=4, column=2, padx=3, pady=3)

substraction_button = Button(root,
                        text="-",
                        width=10,
                        borderwidth=0,
                        cursor="hand2",
                        command=lambda : sub()).grid(row=4, column=3, padx=3, pady=3)

button_1 = Button(root,
                text="1",
                width=10,
                borderwidth=0,
                cursor="hand2",
                command=lambda : data_entry(1)).grid(row=5, column=0, padx=3, pady=3)

button_2 = Button(root,
                text="2",
                width=10,
                borderwidth=0,
                cursor="hand2",
                command=lambda : data_entry(2)).grid(row=5, column=1, padx=3, pady=3)

button_3 = Button(root,
                text="3",
                width=10,
                borderwidth=0,
                cursor="hand2",
                command=lambda : data_entry(3)).grid(row=5, column=2, padx=3, pady=3)

multiplication_button = Button(root,
                        text="x",
                        width=10,
                        borderwidth=0,
                        cursor="hand2",
                        command=lambda : mult()).grid(row=5, column=3, padx=3, pady=3)
decimal_button = Button(root,
                        text=".",
                        width=10,
                        borderwidth=0,
                        cursor="hand2",
                        command= lambda:data_entry(".")).grid(row=6,column=0, padx=3, pady=3)
button_0 = Button(root,
                text="0",
                width=10,
                borderwidth=0,
                cursor="hand2",
                command=lambda : data_entry(0)).grid(row=6, column=1, padx=3, pady=3)

equal_button = Button(root,
                        text="=",
                        width=10,
                        borderwidth=0,
                        cursor="hand2",
                        command= lambda : equal()).grid(row=6,column=2, padx=3, pady=3)

division_button = Button(root,
                        text="/",
                        width=10,
                        borderwidth=0,
                        cursor="hand2",
                        command= lambda : div()).grid(row=6,column=3, padx=3, pady=3)

root.mainloop()                   


