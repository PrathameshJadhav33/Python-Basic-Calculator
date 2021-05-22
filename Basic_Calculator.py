import tkinter as tkinter

root=tkinter.Tk()
root.resizable(False,False)

# Gets the width and height of tk window
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page
root.geometry("+{}+{}".format(positionRight, positionDown))

# Entry widget variables 
x_val=tkinter.StringVar() 
y_val=tkinter.StringVar()

x_label=tkinter.Label(root,text="X",font=(50))
x_label.grid(row=0,column=1,padx=5,pady=5)

# Entry widget of user input
x_entry=tkinter.Entry(root,textvariable=x_val,justify="right",font=(50),relief='solid')
x_entry.grid(row=0,column=2,columnspan=3,padx=(5,15))

y_label=tkinter.Label(root,text="Y",font=(50))
y_label.grid(row=1,column=1,padx=5,pady=5)

# Entry widget of user input
y_entry=tkinter.Entry(root,textvariable=y_val,justify="right",font=(50),relief='solid')
y_entry.grid(row=1,column=2,columnspan=3,padx=(5,15))

# Function to set x_entry to result and y_entry to 0 after deleting their previous content 
def common(res):
    x_entry.delete(0,len(x_val.get()))
    y_entry.delete(0,len(y_val.get()))
    x_entry.insert(0,res)
    y_entry.insert(0,'0')

def divide():
    # here x and y will have values entered in x_entry and y_entry
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x/y")
    common(result)

# Button for division
div_btn=tkinter.Button(root,text="/",font=(50),width=5,command=divide,relief='groove')
div_btn.grid(row=2,column=1,pady=5,padx=(15,5))

def mul():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x*y")
    common(result)

# Button for multiplication
mul_btn=tkinter.Button(root,text="x",font=(50),width=5,command=mul,relief='groove')
mul_btn.grid(row=2,column=2,padx=2)

def add():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x+y")
    common(result)

# Button for addition
add_btn=tkinter.Button(root,text="+",font=(50),width=5,command=add,relief='groove')
add_btn.grid(row=2,column=3,padx=2)

def subs():
    x=float(x_val.get())
    y=float(y_val.get())
    result=eval("x-y")
    common(result)

# Button for substraction
subs_btn=tkinter.Button(root,text="-",font=(50),width=5,command=subs,relief='groove')
subs_btn.grid(row=2,column=4,padx=(0,15))

# function to clear both Entry widgets and set them to 0
def clr():
    x_entry.delete(0,len(x_val.get()))
    y_entry.delete(0,len(y_val.get()))
    x_entry.insert(0,'0')
    y_entry.insert(0,'0')

# Button to call clr() function
clear_btn=tkinter.Button(root,text="Clear",font=(50),width=26,command=clr,relief='groove')
clear_btn.grid(row=3,column=1,columnspan=4,padx=(15,15),pady=10)

# Here clr() is invoked to set both Entry widgets to 0 when application is launched
clr()
root.mainloop()

# Future improvements - 
# 1. Add error handiling.
# 2. Add more functions e.g. - sqrt(),log(),pow().
# 3. Improve GUI by adding hover effects, background images etc.