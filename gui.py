from tkinter import *
import tkinter.ttk as ttk
from config import *
from data import read_data_from_db, write_data_to_db

def gui():
    text = ""
    
    root = Tk()
    root.geometry("400x300")
    
    firstFrame = Frame(root)
    firstFrame.pack(side=TOP)

    secondFrame = Frame(root)
    secondFrame.pack()

    thirdFrame = Frame(root)
    thirdFrame.pack(side=BOTTOM)

    def return_data(data):
        nonlocal text
        text = read_data_from_db(data)
        if text == None:
            text = "Enter correct webpage name, please"
        l.config(text=text)

    combobox = ttk.Combobox(firstFrame, values=sites_for_combobox, width=35)
    
    v = StringVar()
    e = Entry(secondFrame, textvariable=v, width=28)
    v.set(default_entry_message)

    bc = Button(secondFrame, text=choose_button, command = lambda: return_data(v.get()))
    
    load_button = Button(thirdFrame, text=load_from_db, command = lambda: write_data_to_db(combobox.get() or v.get(), ))
    view_from_db_button = Button(thirdFrame, text=view_from_db, command = lambda: return_data(combobox.get() or v.get()))

    l = Label(thirdFrame, wraplength=350)

    combobox.grid(row=0)
    
    bc.grid(row=1, column=1)
    e.grid(row=1, column=0)
    
    load_button.grid(row=2, column=0)
    view_from_db_button.grid(row=2, column=1)
    
    l.grid(row=3, columnspan=2)

    root.mainloop()
