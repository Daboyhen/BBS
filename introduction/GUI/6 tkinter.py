import tkinter as tk
from tkinter import ttk



root =tk.Tk()

#1.using a keyword arguments

ttk.Label(root ,text ='tomorrow is thursday').pack()

#2.using dictionary index after idget creation

#label = ttk.Label(root)
#label['text']='Tomorrow is Thursday'
#label.pack()
#3.using the config(method with keyword attributes)
label =ttk.Label(root)
label.config(text ='tomorrow is thursday')
label.pack()
root.geometry('600x400+50+50')
root.mainloop()