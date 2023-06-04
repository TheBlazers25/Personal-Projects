from tkinter import *
import tkinter as tk
import os

window = tk.Tk()
window.title("To-Do List")
window.geometry('300x330')

top = Frame(window)
top.pack(side=TOP)

bottom = Frame(window)
bottom.pack(padx=31, side=BOTTOM, fill=BOTH, expand=True)

def add_task():
    if task_entry.get():
        task_list.insert(END, '- ' + task_entry.get())
        task_entry_prompt.config(text='Task added successfully')
    else:
        task_entry_prompt.config(text='Cannot add empty task')
    task_entry.delete(0, END)


def delete_task():
    task_list.delete(task_list.curselection())
    task_entry_prompt.config(text='Selected task deleted successfully')


def clear_list():
    task_list.delete(0, END)
    task_entry_prompt.config(text='List cleared successfully')


task_list = Listbox(window, height=13, width=40)
task_list.pack(in_=top, side=TOP)

task_entry = tk.Entry(window, width=40)
task_entry.pack(in_=top, side=BOTTOM)

task_entry_prompt = Label(window, text='')
task_entry_prompt.pack()

add_task = tk.Button(window, text='Add Task', command=add_task)
add_task.pack(in_=bottom, side=LEFT)

delete_task = tk.Button(window, text='Delete Selected Task', command=delete_task)
delete_task.pack(in_=bottom, side=LEFT)

clear_list = tk.Button(window, text='Clear List', command=clear_list)
clear_list.pack(in_=bottom, side=LEFT)

window.mainloop()
