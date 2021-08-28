import tkinter as tk
from cal_UI_Number import Number
from cal_UI_Menu import cal_menu

def run_cal():
    root=tk.Tk(className='calculator')
    root.geometry('330x480')
    display=tk.Text(root,width=330,height=5,undo=True)
    display.pack(side='top')
    Number(root,display)
    cal_menu(root)
    root.mainloop()

run_cal()
# %%
