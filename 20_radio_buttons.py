import tkinter as tk

window=tk.Tk()

rdbtnset=tk.IntVar()

rbdtls={1:'pizza',2:'pasta',3:'burger',4:'submarine'}

def func():

    global rbdtls
    
    x=rdbtnset.get()
    label1.config(text=str(rbdtls[x]))

rb1=tk.Radiobutton(window,text='pizza',variable=rdbtnset,value=1,command=func,font='Helvetica 15 bold')
rb1.pack(anchor=tk.W)

rb2=tk.Radiobutton(window,text='pasta',variable=rdbtnset,value=2,command=func,font='Helvetica 15 bold')
rb2.pack(anchor=tk.W)

rb3=tk.Radiobutton(window,text='burger',variable=rdbtnset,value=3,command=func,font='Helvetica 15 bold')
rb3.pack(anchor=tk.W)

rb4=tk.Radiobutton(window,text='submarine',variable=rdbtnset,value=4,command=func,font='Helvetica 15 bold')
rb4.pack(anchor=tk.W)

label1=tk.Label(window,text='selected food',font='Helvetica 15 bold')
label1.pack()

window.mainloop()
