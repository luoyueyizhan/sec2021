import tkinter as tk
from tkinter.constants import DISABLED, END, INSERT, S
from typing import Text
from cal_cal import Calculator

class Number:
    """Number.

    the number keyboard of the calculator.

    Args:
      master(Tk):the window.
      keyboard(Frame):a box to put the buttons of number.
      display(Text):the text box below the keyboard.
      button_C(Button):a button used to clear the text box.
      button_division(Button):a button used to input /.
      button_maltiplication(Button):a button used to input x.
      button_delete(Button):a button used to get back to last step.
      button_1(Button):a button used to input 1.
      button_2(Button):a button used to input 2.
      button_3(Button):a button used to input 3.
      button_4(Button):a button used to input 4.
      button_5(Button):a button used to input 5.
      button_6(Button):a button used to input 6.
      button_7(Button):a button used to input 7.
      button_8(Button):a button used to input 8.
      button_9(Button):a button used to input 9.
      button_0(Button):a button used to input 0.
      button_bracket_r(Button):a button used to input (.
      button_bracket_l(Button):a button used to input ).
      button_substraction(Button): a button used to input -.
      button_addtion(Button): a button used to input +
      self.button_equal(Button): a button used to input = and order the calculator work.
      button_dot(Button): a button used to input '.'.
    """
    def __init__(self,master,display):
        keyboard=tk.Frame(master)
        keyboard.pack(side='bottom')
        self.display=display
        self.button_C=tk.Button(keyboard,text='C',width=10,height=4,command=self.command_C)
        self.button_C.grid(row=1,column=1)

        self.button_division=tk.Button(keyboard,text='÷',width=10,height=4,command=self.command_division)
        self.button_division.grid(row=1,column=2)

        self.button_multiplication=tk.Button(keyboard,text='x',width=10,height=4,command=self.command_multi)
        self.button_multiplication.grid(row=1,column=3)

        self.button_delete=tk.Button(keyboard,text='backout',width=10,height=4,command=self.command_delete)
        self.button_delete.grid(row=1,column=4)

        self.button1=tk.Button(keyboard,text='1',width=10,height=4,command=self.command_1)
        self.button1.grid(row=2,column=1)

        self.button2=tk.Button(keyboard,text='2',width=10,height=4,command=self.command_2)
        self.button2.grid(row=2,column=2)

        self.button3=tk.Button(keyboard,text='3',width=10,height=4,command=self.command_3)
        self.button3.grid(row=2,column=3)

        self.button4=tk.Button(keyboard,text='4',width=10,height=4,command=self.command_4)
        self.button4.grid(row=3,column=1)

        self.button5=tk.Button(keyboard,text='5',width=10,height=4,command=self.command_5)
        self.button5.grid(row=3,column=2)

        self.button6=tk.Button(keyboard,text='6',width=10,height=4,command=self.command_6)
        self.button6.grid(row=3,column=3)

        self.button7=tk.Button(keyboard,text='7',width=10,height=4,command=self.command_7)
        self.button7.grid(row=4,column=1)

        self.button8=tk.Button(keyboard,text='8',width=10,height=4,command=self.command_8)
        self.button8.grid(row=4,column=2)

        self.button9=tk.Button(keyboard,text='9',width=10,height=4,command=self.command_9)
        self.button9.grid(row=4,column=3)

        self.bracket_l=tk.Button(keyboard,text='(',width=10,height=4,command=self.command_bracket_l)
        self.bracket_l.grid(row=5,column=1)

        self.button0=tk.Button(keyboard,text='0',width=10,height=4,command=self.command_0)
        self.button0.grid(row=5,column=2)

        self.button_bracket_r=tk.Button(keyboard,text=')',width=10,height=4,command=self.command_bracket_r)
        self.button_bracket_r.grid(row=5,column=3)

        self.button_substraction=tk.Button(keyboard,text='-',width=10,height=4,command=self.command_sbustraction)
        self.button_substraction.grid(row=2,column=4)

        self.button_addtion=tk.Button(keyboard,text='+',width=10,height=4,command=self.command_addion)
        self.button_addtion.grid(row=3,column=4)
        
        self.button_equal=tk.Button(keyboard,text='=',width=10,height=4,command=self.command_equal)
        self.button_equal.grid(row=4,column=4)

        self.button_dot=tk.Button(keyboard,text='.',width=10,height=4,command=self.command_dot)
        self.button_dot.grid(row=5,column=4)

    def command_1(self):
        """

        print '1' in the text box.

        """
        self.display.insert(tk.END,'1')

    def command_2(self):
        """

        print '2' in the text box.

        """
        self.display.insert(tk.END,'2')

    def command_3(self):
        """

        print '3' in the text box.

        """
        self.display.insert(tk.END,'3')

    def command_4(self):
        """

        print '4' in the text box.

        """
        self.display.insert(tk.END,'4')

    def command_5(self):
        """

        print '5' in the text box.

        """
        self.display.insert(tk.END,'5')

    def command_6(self):
        """

        print '6' in the text box.

        """
        self.display.insert(tk.END,'6')

    def command_7(self):
        """

        print '7' in the text box.

        """
        self.display.insert(tk.END,'7')

    def command_8(self):
        """

        print '8' in the text box.

        """
        self.display.insert(tk.END,'8')

    def command_9(self):
        """

        print '9' in the text box.

        """
        self.display.insert(tk.END,'9')

    def command_bracket_l(self):
        """

        print '(' in the text box.

        """
        self.display.insert(tk.END,'(')

    def command_bracket_r(self):
        """

        print ')' in the text box.

        """
        self.display.insert(tk.END,')')

    def command_C(self):
        """

        clear text box.

        """
        self.display.delete(1.0,tk.END)

    def command_division(self):
        """

        print '/' in the text box.

        """
        self.display.insert(tk.END,'/')

    def command_multi(self):
        """

        print 'x' in the text box.

        """
        self.display.insert(tk.END,'x')

    def command_delete(self):
        """

        get back to the last step.

        """
        self.display.edit_undo()

    def command_sbustraction(self):
        """

        print '-' in the text box.

        """
        self.display.insert(tk.END,'-')

    def command_addion(self):
        """

        print '+' in the text box.

        """
        self.display.insert(tk.END,'+')

    def command_equal(self):
        """

        print '=' in the text box and order the calculator work.

        """
        equation=self.display.get(1.0,tk.END)
        calculator=Calculator(equation,self.display)
        calculator.main()
    
    def command_0(self):
        """

        print '0' in the text box.

        """
        self.display.insert(tk.END,'0')

    def command_dot(self):
        """

        print '.' in the text box.
        
        """
        self.display.insert(tk.END,'.')

