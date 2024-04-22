import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning !!", "You must enter a task.")
        
def delete_task():
    try:
        selected = listbox.curselection()
        if selected:
            messagebox.showwarning(selected,' Are you Sure to delete !!')
            listbox.delete(selected)
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")
    except:
        messagebox.showwarning("Warning", "Error Occured")

def edit_task():
    try:
        selected = listbox.curselection()
        if selected:
            task = listbox.get(selected)
            new_task = simpledialog.askstring("Edit Task", "Edit your task:", initialvalue=task)
            if new_task:
                listbox.delete(selected)
                listbox.insert(selected, new_task)
        else:
            messagebox.showwarning("Warning", "You must select a task to edit.")
    except:
        messagebox.showwarning("Warning", "Error Occured")
        
window = tk.Tk();
window.title('TO-DO LIST')
window.configure(bg='ivory')

window.geometry("700x500")

label_1 = tk.Label(window,text='To-Do List',font=('consolas',35,'bold'),fg='black',bg='yellow',width=100,height=2)
label_1.pack()

label_2 = tk.Label(window,text='Enter Task to Add : ',font=('consolas',15),fg='purple')
label_2.place(x=10,y=130)

entry = tk.Entry(window,font = ('consolas',25),fg = 'black')
entry.place(x=10,y=170)

add = tk.Button(window,text = "Add",bg ='seagreen',fg='black',font = ('consolas',14),command = add_task)
add.place(x=400,y=170)

edit = tk.Button(window,text = "Edit",bg ='skyblue',fg='black',font = ('consolas',14),command = edit_task)
edit.place(x=470,y=170)

delete = tk.Button(window,text = "Delete",bg ='orange',fg='black',font = ('consolas',14),command = delete_task)
delete.place(x=550,y=170)

label_3 = tk.Label(window,text='Tasks to Do !!',fg = 'purple',font=('consolas',25))
label_3.place(x=10,y=240)

listbox = tk.Listbox(window,width = 100,fg = 'black',font = ('consolas',25),bg = 'lemonchiffon')
listbox.place(x=10,y=300)
               
window.mainloop()
