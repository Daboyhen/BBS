import tkinter as tk
from tkinter import ttk



root =tk.Tk()


tk.Label(root ,text ='today is wednesday').pack()
ttk.Label(root ,text ='tomorrow is thursday').pack()

root.geometry('600x400+50+50')
root.mainloop()