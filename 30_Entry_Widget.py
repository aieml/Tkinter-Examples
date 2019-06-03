import tkinter as tk

window=tk.Tk()

def getEntries():

    name=entry1.get()
    age=entry2.get()

    print(name,age)

label1=tk.Label(window,text='Name:',font='Helvetica 15')
label1.grid(row=0,column=0)

entry1=tk.Entry(window)
entry1.grid(row=0,column=1)

label2=tk.Label(window,text='Age:',font='Helvetica 15')
label2.grid(row=1,column=0)

entry2=tk.Entry(window)
entry2.grid(row=1,column=1)

button1=tk.Button(window,text='Enter',command=getEntries)
button1.grid(row=2,column=0)

window.mainloop()
