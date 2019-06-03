import tkinter as tk
import time as t

window=tk.Tk()
window.title('COUNTER (powered by tkinter)')    #window title
count=0

def func1():
    window.destroy()
##    global count
##    label.config(text=str(count))
##    count=count+1

def func2():

    global count
    count=0

def counter():

    global count
    if(count>20):
        label.config(fg='red')
    elif(count>10):
        label.config(fg='blue')
        
    label.config(text=str(count))
    count=count+1
    window.after(200,counter)

logo=tk.PhotoImage(file='python.gif')   #path to the photo
#logo.zoom(2,2)

label=tk.Label(window,text=str(count),fg='green',font='Helvetica 50 bold')
#label.pack()
label.grid(row=0,column=0)

label1=tk.Label(window,text='python logo',image=logo,height=100,width=400)
#label1.pack(side='right')
label1.grid(row=1,column=0)

btn=tk.Button(window,text='stop',fg='white',bg='red',command=func1,font='Helvetica 20 bold',height=1,width=10)
btn.grid(row=2,column=0)

btn1=tk.Button(window,text='reset',fg='white',bg='green',command=func2,font='Helvetica 20 bold',height=1,width=10)
btn1.grid(row=2,column=1)

counter()

window.mainloop()
