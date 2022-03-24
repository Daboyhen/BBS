#tkinter entry widget example
import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo

#create the root window
root =tk.Tk()
root.geometry('600x400+50+50')
root.resizable(False, False)
root.title('Digikids Application: Sign in')


#store the mail and the password
email =tk.StringVar()
password =tk.StringVar()

def login_clicked():
    '''
    callback when the login button is clicked
    '''
    msg =f'you entered email: {email()} and password: {password.get()}'
    showinfo(
        title ='information',
        message =msg
    )

    #The sign in frame 
signin =ttk.Frame(root)
signin.pack(padx =10, pady =10, fill ='x', expand =True)

    #the email label widget
email_label = ttk.Label(signin, text= 'email address')
email_label.pack(fill='x', expand =True)

email_entry =ttk.Entry(signin, textvariable =email)
email_entry.pack(fill ='x',expand =True)
email_entry.focus()

    #The passsword label widget
password_label =ttk.Label(signin, text ='password:')
password_label.pack(fill ='x',expand =True)

password_entry =ttk.Entry(signin, textvariable = password, show='*')
password_entry.pack(fill ='x',expand = True)

    #create the login button
login_button =ttk.Button(signin,text='login',command=login_clicked)
login_button.pack(fill='x',expand = True,pady =10)

root.mainloop()