import tkinter as tk
from tkinter import *
import random
import string

password = ""

def Generate_password():
    global password
    try:
        if entry_1.get() and entry_2.get():
            length = int(entry_2.get())
            l = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(l) for i in range(length))
            password1 = "The Password Generated is :  "+password
            label_3.config(text=password1,fg='red')
        elif entry_2.get():
            password = "Enter User Name !!"
            label_3.config(text=password,fg='red')
        else:
            password = "Enter Desired Length of Password !!"
            label_3.config(text=password,fg='red')            
    except ValueError:
        print("Please enter a valid integer for the password length.")
        
def Reset():
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    label_3.config(text="")
    label_4.config(text="")

def Accept():
    global password
    s = "Hello "+entry_1.get()+"! your Password is :  "+password
    label_4.config(text=s)

window = tk.Tk()
window.geometry('500x500')
window.configure(bg='lavender')

label_1 = tk.Label(window,text="PASSWORD GENERATOR",font=("Rockwell",40,"bold"),fg="black",bg='lavender')
label_1.place(x=450,y=4)

label_2 = tk.Label(window,text="Enter  User  Name  : ",font=("rockwell",25),fg="black",bg='lavender')
label_2.place(x=350,y=150)

entry_1 = tk.Entry(window,font=('rockwell',23))
entry_1.place(x=680,y=155)

label_2 = tk.Label(window,text= "Enter  the  desired  length  of  the  password  :",font=("rockwell",25),bg='lavender')
label_2.place(x=200,y=250)
    
entry_2 = tk.Entry(window,font=('rockwell',20))
entry_2.place(x=930,y=260)

button_1 = tk.Button(window,text="GENERATE",font=('rockwell',20,"bold"),bg='lightpink',command=Generate_password)
button_1.place(x=300,y=400)

button_2 = tk.Button(window,text="ACCEPT",font=('rockwell',20,"bold"),bg='lightgreen',command=Accept)
button_2.place(x=640,y=400)

button_3 = tk.Button(window,text=" RESET ",font=('rockwell',20,"bold"),bg='gold',command=Reset)
button_3.place(x=950,y=400)

label_3 = tk.Label(window,font=("rockwell",25,"bold"),bg='lavender')
label_3.place(x=300,y=550)

label_4 = tk.Label(window,font=("rockwell",25,"bold"),bg='lavender')
label_4.place(x=300,y=650)

window.mainloop()
