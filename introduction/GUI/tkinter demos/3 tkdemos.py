from cProfile import label
import tkinter as tk
class Window(tk.TK):
    def __init__(self):
        super().__init__()
        self.title('digikids application')

        label= tk.Label(self, text='welcome to digikids')
        label.pack(fill=tk.Both, expand=1, padx=200, pady=100)

if __name__=='__main__':
    window =Window()
    window.mainloop()