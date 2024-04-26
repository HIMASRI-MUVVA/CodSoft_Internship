import tkinter as tk

value = " "
def display(key):
    global value
    value += key
    label_1.config(text = value)

def result():
    global value
    result = ""
    if value != "":
        try:
            result = str(eval(value))
        except:
            result = "Error"
            value = ""
        label_1.config(text = result)

def clear():
    global value
    value = ""
    label_1.config(text = value,)    
    

window = tk.Tk()
window.title("SIMPLE CALCULATOR")
window.configure(bg='ivory')

label_1 = tk.Label(window,width = 27,height=3,font = ("consolas",20,"bold"),bg='grey4',fg='white')

label_1.grid(row=0,column=0,columnspan=5)



buttons = ['C', ' (', ' )', ' /',
           '7', '8', '9',' *',
           '4', '5', '6', '+',
           '1', '2', '3', ' -',
           ' .', '0','%', '=']

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: display(x) if x not in ['=', 'C'] else result() if x == '=' else clear()
    if button=='C':
        tk.Button(window,text=button,bg='blue',padx=21, pady=10,bd=10, font=('Arial',23), command=action).grid(row=row_val, column=col_val)
        col_val += 1
    elif button=='=':
        tk.Button(window,text=button,bg='orange',padx=21, pady=10,bd=10, font=('Arial',23), command=action).grid(row=row_val, column=col_val)
        col_val += 1
    else:
        tk.Button(window,text=button,padx=21,bg='grey4',fg='white',pady=10,bd=10,font=('Arial', 20), command=action).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

window.mainloop()
