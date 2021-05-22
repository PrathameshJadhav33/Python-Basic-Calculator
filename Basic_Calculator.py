import tkinter as tkinter

root=tkinter.Tk()

x_val=tkinter.StringVar() 

#root.geometry("300x200")
x_label=tkinter.Label(root,text="X",font=(50))
x_label.grid(row=0,column=1,padx=5,pady=5)

x_entry=tkinter.Entry(root,textvariable=x_val,justify="right",font=(50))
x_entry.grid(row=0,column=2,columnspan=3,padx=(5,15))

y_label=tkinter.Label(root,text="Y",font=(50))
y_label.grid(row=1,column=1,padx=5,pady=5)

y_entry=tkinter.Entry(root,textvariable=x_val,justify="right",font=(50))
y_entry.grid(row=1,column=2,columnspan=3,padx=(5,15))

div_btn=tkinter.Button(root,text="/",font=(50),width=5)
div_btn.grid(row=2,column=1,pady=5,padx=(15,0))

mul_btn=tkinter.Button(root,text="x",font=(50),width=5)
mul_btn.grid(row=2,column=2,padx=2)

add_btn=tkinter.Button(root,text="+",font=(50),width=5)
add_btn.grid(row=2,column=3,padx=2)

subs_btn=tkinter.Button(root,text="-",font=(50),width=5)
subs_btn.grid(row=2,column=4,padx=(0,15))

clear_btn=tkinter.Button(root,text="Clear",font=(50),width=26)
clear_btn.grid(row=3,column=1,columnspan=4,padx=(15,15),pady=10)

root.mainloop()