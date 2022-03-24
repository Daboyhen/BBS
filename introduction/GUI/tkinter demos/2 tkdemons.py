from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master =master


        #widget can take all window
        self.pack(fill=BOTH, expand=1)


        #creat button and link it toclickexitButton
        exitButton =Button(self, text='fit', command=self.clickExitButton)

        #location of the button (x, y)
        exitButton.place(x=160, y=80)
    def clickExitButton(self):
        exit()

root= Tk()
app= Window(root)
root.wm_title('Button Example')
root.geometry('400x200')
root.mainloop()