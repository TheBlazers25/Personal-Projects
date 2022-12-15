from tkinter import *
from tkinter import ttk
import keyboard

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

recorded = keyboard.record(until='esc')

root.mainloop()