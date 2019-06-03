import tkinter as tk
from matplotlib import pyplot as plt

window=tk.Tk()
window.title('XY Plotter')

def getData():

    x=[]
    y=[]

    for i in range(0,5):
        x.append(entries[i].get())
        y.append(entries[i+5].get())

    plt.plot(x,y)
    plt.show()

xlabel=tk.Label(window,text='X Values',font='Helvetica 20 bold')
xlabel.grid(row=0,column=0)

ylabel=tk.Label(window,text='Y Values',font='Helvetica 20 bold')
ylabel.grid(row=0,column=1)

entries=[tk.Entry for i in range(0,10)]

for i in range(0,5):

    entries[i]=tk.Entry(window)
    entries[i].grid(row=i+1,column=0)

    entries[i+5]=tk.Entry(window)
    entries[i+5].grid(row=i+1,column=1)


btn1=tk.Button(window,text='plot',command=getData)
btn1.grid(row=7,column=0)
btn2=tk.Button(window,text='exit',command=window.destroy)
btn2.grid(row=7,column=1)

window.mainloop()
