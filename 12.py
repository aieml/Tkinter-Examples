import tkinter as tk    #in python 2, import Tkinter as tk

status='OFF'

def func1():

    global status

    if(status=='OFF'):
        label1.config(text='Hello, python tkinter',fg='cyan',bg='gray50')         #to modify the label widget after initializing
        btn1.config(text='dont show',fg='green')
        status='ON'

    else:
        label1.config(text='EMPTY LABEL',fg='RoyalBlue1',bg='red')         #to modify the label widget after initializing
        btn1.config(text='show',fg='green')
        status='OFF'
    #print(status)
    
font1='Times 25 bold italic'
font2='Helvetica 15 bold'
font3='Verdana'



window=tk.Tk()  #Tk is the method to initialize the tkinter window

label1=tk.Label(window,text='EMPTY LABEL',fg='RoyalBlue1',bg='red',font=font1)
label1.pack()

btn1=tk.Button(window,text='show',fg='green',font=font2,command=func1)
btn1.pack()

window.mainloop()
