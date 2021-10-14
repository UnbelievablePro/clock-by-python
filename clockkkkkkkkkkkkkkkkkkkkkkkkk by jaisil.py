from tkinter import * 
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("digital super clock")
def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label=Label(root,font=("ds-digital",100), background="blue", foreground="black")
label.pack(anchor='center')
time()
mainloop()


 
