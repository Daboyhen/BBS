from tkinter import *

class window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master =master

#code to intitialize the tkinter 
root =Tk()
app = window(root)


#add the window title
root.wm_title('Digikids Application')


#to show the window and retain it on the screen
root.mainloop