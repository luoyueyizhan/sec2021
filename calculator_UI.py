import tkinter as tk
class Number:
    def __init__(self,master):
        keyboard=tk.Frame(master)
        keyboard.pack(side='bottom')

        self.button_C=tk.Button(keyboard,text='C')
        self.button_C.grid(row=1,column=1,padx=10,pady=10)

        self.button_division=tk.Button(keyboard,text='÷')
        self.button_division.grid(row=1,column=2,padx=10,pady=10)

        self.button_multiplication=tk.Button(keyboard,text='x')
        self.button_multiplication.grid(row=1,column=3,padx=10,pady=10)

        self.button_delete=tk.Button(keyboard,text='delete')
        self.button_delete.grid(row=1,column=4,padx=10,pady=10)

        self.button1=tk.Button(keyboard,text='1')
        self.button1.grid(row=2,column=1,padx=10,pady=10)

        self.button2=tk.Button(keyboard,text='2')
        self.button2.grid(row=2,column=2,padx=10,pady=10)

        self.button3=tk.Button(keyboard,text='3')
        self.button3.grid(row=2,column=3,padx=10,pady=10)

        self.button4=tk.Button(keyboard,text='4')
        self.button4.grid(row=3,column=1,padx=10,pady=10)

        self.button5=tk.Button(keyboard,text='5')
        self.button5.grid(row=3,column=2,padx=10,pady=10)

        self.button6=tk.Button(keyboard,text='6')
        self.button6.grid(row=3,column=3,padx=10,pady=10)

        self.button7=tk.Button(keyboard,text='6')
        self.button7.grid(row=4,column=1,padx=10,pady=10)

        self.button8=tk.Button(keyboard,text='7')
        self.button8.grid(row=4,column=2,padx=10,pady=10)

        self.button9=tk.Button(keyboard,text='9')
        self.button9.grid(row=4,column=3,padx=10,pady=10)

        self.button10=tk.Button(keyboard,text='%')
        self.button10.grid(row=5,column=1,padx=10,pady=10)

        self.button0=tk.Button(keyboard,text='0')
        self.button0.grid(row=5,column=2,padx=10,pady=10)

        self.button_dot=tk.Button(keyboard,text='.')
        self.button_dot.grid(row=5,column=3,padx=10,pady=10)

        self.button_substraction=tk.Button(keyboard,text='-')
        self.button_substraction.grid(row=2,column=4,padx=10,pady=10)

        self.button_addtion=tk.Button(keyboard,text='-')
        self.button_addtion.grid(row=3,column=4,padx=10,pady=10)
        
        self.button_equal=tk.Button(keyboard,text='-')
        self.button_equal.grid(row=4,column=4,padx=10,pady=10)




root=tk.Tk(className='calculator')
root.geometry('500x300')
Number(root)
display=tk.Text(root,height=3)
display.pack(side='top')


