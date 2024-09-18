# Importing tkinter module to create GUI
from tkinter import *
from tkinter import ttk
from math import *

# Creating the window of the app
root = Tk()

# Creating an input field. Two separate functions for updating and removing the button clicks from the input field.
def input_update(text):
  input.insert(END,text)

def clear_input():
  input.delete(0, END)

def sum_input():


input= Entry(root, width= 30, bg= "white")
input.pack()


# Creating dictionary to list out all the different buttons on the calculator
button_dict={}
option = ["+", "-", "=", "%", "*", "C", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Creating for loop to list out all the buttons. 
for i in option:
  if i == "C":
    button_dict[i] = ttk.Button(root, text=i, command=clear_input)
    button_dict[i].pack()
  elif i == "+":
    button_dict[i] = ttk.Button(root, text=i, command= )
  else:
    def func(x=i):
      return input_update(x)
    button_dict[i] = ttk.Button(root, text=i, command=func)
    button_dict[i].pack()


# Create the width and height of the window
root.geometry('400x600')

# Running the app
root.mainloop()