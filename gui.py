from tkinter import *
import tkinter.ttk as ttk
from config import *
from data import read_data_from_db

def gui():
    root = Tk()
    
    firstFrame = Frame(root)
    firstFrame.pack(side=TOP)

    secondFrame = Frame(root)
    secondFrame.pack()

    thirdFrame = Frame(root)
    thirdFrame.pack(side=BOTTOM)

    
    choosen_value = StringVar()
    cb = ttk.Combobox(firstFrame, values=sites_for_combobox, width=20)
    bc = Button(firstFrame, text=choose_button, command=read_data_from_db("ya.ru"))
    
    e = Entry(secondFrame, width=30)
    
    load_button = Button(thirdFrame, text=load_from_db)
    view_from_db_button = Button(thirdFrame, text=view_from_db)
    
    cb.grid(row=0)
    bc.grid(row=0, column=1)
    
    e.grid(row=1, column=0)
    
    load_button.grid(row=2, column=0)
    view_from_db_button.grid(row=2, column=1)
    
    root.mainloop()
