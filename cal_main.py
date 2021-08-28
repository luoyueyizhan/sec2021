import tkinter as tk
from cal_UI_Number import Number
from cal_UI_Menu import cal_menu

def run_cal():
    """Main procedure.

    the main procedure of the calculator.

    Args:
        root(Tk):some value and function of the window.
        display(Text):the text box of the window.
        Number(Number):the number keyborad
        calmenu(calmenu):the menu of the window.
    """
    root=tk.Tk(className='calculator')
    root.geometry('330x480')
    display=tk.Text(root,width=330,height=5,undo=True)
    display.pack(side='top')
    Number(root,display)
    cal_menu(root)
    root.mainloop()

run_cal()
