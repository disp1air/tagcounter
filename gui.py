from tkinter import *
import tkinter.ttk as ttk
from config import *
from data import read_data_from_db, write_data_to_db

def gui():
    root = Tk()
    
    firstFrame = Frame(root)
    firstFrame.pack(side=TOP)

    secondFrame = Frame(root)
    secondFrame.pack()

    thirdFrame = Frame(root)
    thirdFrame.pack(side=BOTTOM)

    resultFrame = Frame(root)
    resultFrame.pack()

    combobox = ttk.Combobox(firstFrame, values=sites_for_combobox, width=30)
    
    bc = Button(secondFrame, text=choose_button)
    e = Entry(secondFrame, width=21)
    
    load_button = Button(thirdFrame, text=load_from_db, command = lambda: write_data_to_db(combobox.get(), ))
    view_from_db_button = Button(thirdFrame, text=view_from_db, command = lambda: read_data_from_db(combobox.get()))
    
    combobox.grid(row=0)
    
    bc.grid(row=1, column=1)
    e.grid(row=1, column=0)
    
    load_button.grid(row=2, column=0)
    view_from_db_button.grid(row=2, column=1)
    
    Label(resultFrame, text = {"a": 11, "b": 22})

    root.mainloop()
