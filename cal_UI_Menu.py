from cal_history import read_history
import tkinter as tk

class cal_menu:
    def __init__(self,master):
        menubar=tk.Menu(master)
        self.root=master
        filemenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='File',menu=filemenu)
        filemenu.add_command(label='New',command=self.command_C)
        filemenu.add_command(label='history',command=self.command_history)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',command=master.quit)

        helpmenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='help',menu=helpmenu)
        helpmenu.add_command(label='getback',command=self.command_delete)
        helpmenu.add_command(label='readme',command=self.command_readme)

        master.config(menu=menubar)

    def command_history(self):
        read_history()
    
    def command_readme(self):
        window_help=tk.Toplevel(self.root)
        window_help.geometry('300x200')
        window_help.title('help')
        label_readme=tk.Label(window_help,text='Readme获取方式')
        label_email=tk.Label(window_help,text='邮箱：luoyeyizhan@163.com')
        label_Git=tk.Label(window_help,text='GitHub地址：https://github.com/luoyueyizhan/sec2021.git')
        label_readme.pack()
        label_email.pack()
        label_Git.pack()

    def command_C(self):
        self.display.delete(1.0,tk.END)

    def command_delete(self):
        self.display.edit_undo()
