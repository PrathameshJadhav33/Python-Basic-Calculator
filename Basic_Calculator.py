import tkinter as tkinter

root=tkinter.Tk()

x_val=tkinter.StringVar() 
y_val=tkinter.StringVar()

#root.geometry("300x200")
x_label=tkinter.Label(root,text="X",font=(50))
x_label.grid(row=0,column=1,padx=5,pady=5)

x_entry=tkinter.Entry(root,textvariable=x_val,justify="right",font=(50))
x_entry.grid(row=0,column=2,columnspan=3,padx=(5,15))

y_label=tkinter.Label(root,text="Y",font=(50))
y_label.grid(row=1,column=1,padx=5,pady=5)

y_entry=tkinter.Entry(root,textvariable=y_val,justify="right",font=(50))
y_entry.grid(row=1,column=2,columnspan=3,padx=(5,15))

def divide():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x/y")
    x_entry.delete(0,len(x_val.get()))
    y_entry.delete(0,len(y_val.get()))
    x_entry.insert(0,result)

div_btn=tkinter.Button(root,text="/",font=(50),width=5,command=divide)
div_btn.grid(row=2,column=1,pady=5,padx=(15,0))

def mul():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x*y")
    x_entry.delete(0,len(x_val.get()))
    y_entry.delete(0,len(y_val.get()))
    x_entry.insert(0,result)

mul_btn=tkinter.Button(root,text="x",font=(50),width=5,command=mul)
mul_btn.grid(row=2,column=2,padx=2)

def add():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x+y")
    x_entry.delete(0,len(x_val.get()))
    y_entry.delete(0,len(y_val.get()))
    x_entry.insert(0,result)

add_btn=tkinter.Button(root,text="+",font=(50),width=5,command=add)
add_btn.grid(row=2,column=3,padx=2)

def subs():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x-y")
    x_entry.delete(0,len(x_val.get()))
    y_entry.delete(0,len(y_val.get()))
    x_entry.insert(0,result)

subs_btn=tkinter.Button(root,text="-",font=(50),width=5,command=subs)
subs_btn.grid(row=2,column=4,padx=(0,15))

def clr():
    x_entry.delete(0,len(x_val.get()))
    y_entry.delete(0,len(y_val.get()))
    x_entry.insert(0,'0')
    y_entry.insert(0,'0')

clear_btn=tkinter.Button(root,text="Clear",font=(50),width=26,command=clr)
clear_btn.grid(row=3,column=1,columnspan=4,padx=(15,15),pady=10)

root.mainloop()