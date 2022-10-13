#importing neccessary functions

from tkinter import *
from tkinter.ttk import *

#importing time

from time import strftime

root = Tk()          #creating UI
root.title("Clock")  #csetting up the title

#defining a function to get time

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

#creating a label to store clock

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')
time()

mainloop()
