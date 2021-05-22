import tkinter as tkinter

root=tkinter.Tk()
root.resizable(False,False)
x_val=tkinter.StringVar() 
y_val=tkinter.StringVar()

#root.geometry("300x200")
x_label=tkinter.Label(root,text="X",font=(50))
x_label.grid(row=0,column=1,padx=5,pady=5)

x_entry=tkinter.Entry(root,textvariable=x_val,justify="right",font=(50),relief='solid')
x_entry.grid(row=0,column=2,columnspan=3,padx=(5,15))

y_label=tkinter.Label(root,text="Y",font=(50))
y_label.grid(row=1,column=1,padx=5,pady=5)

y_entry=tkinter.Entry(root,textvariable=y_val,justify="right",font=(50),relief='solid')
y_entry.grid(row=1,column=2,columnspan=3,padx=(5,15))

def common(res):
    x_entry.delete(0,len(x_val.get()))
    y_entry.delete(0,len(y_val.get()))
    x_entry.insert(0,res)
    y_entry.insert(0,'0')

def divide():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x/y")
    common(result)

div_btn=tkinter.Button(root,text="/",font=(50),width=5,command=divide,relief='groove')
div_btn.grid(row=2,column=1,pady=5,padx=(15,5))

def mul():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x*y")
    common(result)

mul_btn=tkinter.Button(root,text="x",font=(50),width=5,command=mul,relief='groove')
mul_btn.grid(row=2,column=2,padx=2)

def add():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x+y")
    common(result)

add_btn=tkinter.Button(root,text="+",font=(50),width=5,command=add,relief='groove')
add_btn.grid(row=2,column=3,padx=2)

def subs():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x-y")
    common(result)

subs_btn=tkinter.Button(root,text="-",font=(50),width=5,command=subs,relief='groove')
subs_btn.grid(row=2,column=4,padx=(0,15))

def clr():
    x_entry.delete(0,len(x_val.get()))
    y_entry.delete(0,len(y_val.get()))
    x_entry.insert(0,'0')
    y_entry.insert(0,'0')

clear_btn=tkinter.Button(root,text="Clear",font=(50),width=26,command=clr,relief='groove')
clear_btn.grid(row=3,column=1,columnspan=4,padx=(15,15),pady=10)

clr()
root.mainloop()