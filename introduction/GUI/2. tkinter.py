import tkinter as tk

root = tk.Tk()
root.title('centering the Tkinter window')

window_width =600
window_height =400


#get the screen dimension
screen_width =root.winfo_screenwidth()
screen_height =root.winfo_screenheight()

#Finding tne center point
center_x = int(screen_width/2 -window_width /2)
center_y = int(screen_width/2 -window_width /2)

#set the position of the window to the center of screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.mainloop()