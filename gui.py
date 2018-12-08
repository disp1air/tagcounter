from tkinter import *
import tkinter.ttk as ttk
from config import *
from pick import read_data_from_db, write_data_to_db

def gui():
    root = Tk()
    
    firstFrame = Frame(root)
    firstFrame.pack(side=TOP)

    secondFrame = Frame(root)
    secondFrame.pack()

    thirdFrame = Frame(root)
    thirdFrame.pack(side=BOTTOM)

    combobox = ttk.Combobox(firstFrame, values=sites_for_combobox, width=20)
    bc = Button(firstFrame, text=choose_button)

    e = Entry(secondFrame, width=30)
    
    load_button = Button(thirdFrame, text=load_from_db, command = lambda: write_data_to_db(combobox.get(), ))
    view_from_db_button = Button(thirdFrame, text=view_from_db, command = lambda: read_data_from_db(combobox.get()))
    
    combobox.grid(row=0)
    bc.grid(row=0, column=1)
    
    e.grid(row=1, column=0)
    
    load_button.grid(row=2, column=0)
    view_from_db_button.grid(row=2, column=1)
    
    root.mainloop()
