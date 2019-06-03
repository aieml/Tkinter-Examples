import tkinter as tk

window=tk.Tk()
window.title('Calculator(powered by tkinter)')

eqn=' '
display=tk.StringVar()

def btnPrs(btn):

    global eqn
    global dispaly
    
    if(btn=='C'):
        eqn=' '
        display.set('0')

    elif(btn=='='):
        total=eval(eqn)
        display.set(str(total))
        eqn=' '
    
    else:
        eqn=eqn+btn
        display.set(eqn)

display.set('0')

label_calculation=tk.Label(window,textvariable=display,font='Helvetica 12',bg='white',width=20,height=1)
label_calculation.grid(row=0,columnspan=8,padx=5,pady=3)


buttons=[[tk.Button for i in range(0,4)]for j in range(0,4)]

button_details={0:{0:'1',1:'2',2:'3',3:'+'},1:{0:'4',1:'5',2:'6',3:'-'},2:{0:'7',1:'8',2:'9',3:'x'},3:{0:'C',1:'0',2:'=',3:'/'}}

for i in range(0,4):
    for j in range (0,4):
        buttons[i][j]=tk.Button(window,text=button_details[i][j],font='Helvetica 12 bold',width=2,height=1)
        buttons[i][j].grid(row=i+1,column=j,padx=8,pady=8)
        
buttons[3][0].config(bg='red')

buttons[0][0].config(command=lambda:btnPrs('1'))
buttons[0][1].config(command=lambda:btnPrs('2'))
buttons[0][2].config(command=lambda:btnPrs('3'))
buttons[0][3].config(command=lambda:btnPrs('+'))
buttons[1][0].config(command=lambda:btnPrs('4'))
buttons[1][1].config(command=lambda:btnPrs('5'))
buttons[1][2].config(command=lambda:btnPrs('6'))
buttons[1][3].config(command=lambda:btnPrs('-'))
buttons[2][0].config(command=lambda:btnPrs('7'))
buttons[2][1].config(command=lambda:btnPrs('8'))
buttons[2][2].config(command=lambda:btnPrs('9'))
buttons[2][3].config(command=lambda:btnPrs('*'))
buttons[3][0].config(command=lambda:btnPrs('C'))
buttons[3][1].config(command=lambda:btnPrs('0'))
buttons[3][2].config(command=lambda:btnPrs('='))
buttons[3][3].config(command=lambda:btnPrs('/'))

window.mainloop()
