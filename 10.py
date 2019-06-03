import tkinter as tk    #in python 2, import Tkinter as tk

font1='Times 25 bold italic'
font2='Helvetica'
font3='Verdana'

window=tk.Tk()  #Tk is the method to initialize the tkinter window

label1=tk.Label(window,text='Hello python, tkinter',fg='RoyalBlue1',bg='red',font=font1)
label1.pack()

window.mainloop()
