import tkinter as tk
from tkinter import ttk 

root =tk.Tk()

def button_clicked():
    print('you have clicked the button')
    
button =ttk.Button(root, text='please click here',\
    command=button_clicked)
button.pack()

root.geometry('600x400+50+50')
root.mainloop()
