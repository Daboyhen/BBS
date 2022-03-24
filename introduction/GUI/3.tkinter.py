import tkinter as tk

root =tk.Tk()
root.title('digikids example 3')
root.geometry('600x400+50+50')
#resizable() has two parameters that specify the width and
#heightof the window, you specify if it is resizable or not

root.resizable(False,False)
root.attributes('-alpha', 0.5)#defining the transparency
#root.attributes('-topmost',0)  #defines the windows stack order
root.mainloop()