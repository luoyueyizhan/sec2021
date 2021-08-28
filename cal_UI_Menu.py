from cal_history import read_history
import tkinter as tk

class cal_menu:
    """Menu.

    The menu of the window.
    
    Args:
        master(Tk):the window
        menubar(Menu):the menu box
        root(Tk):the window
        filemenu(Menu):a smaller menubox on the menubar
        helpmenu(Menu):a smaller menubox on the menubar
    """
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
        """

        show the history.

        """
        read_history(self.root)
    
    def command_readme(self):
        """

        show a new window about some contact information of the devoloper.

        Args:
          window_help(Toplevel):a new window.
          label_readme(Label):the address of readme.md.
          label_email(Label):the email address of devoloper.
          label_Git(Label):the github address of devoloper.
        """
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
        """

        clear the text box.

        """
        self.display.delete(1.0,tk.END)

    def command_delete(self):
        """

        get back to the last step.
        
        """
        self.display.edit_undo()
