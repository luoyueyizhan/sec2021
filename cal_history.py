import tkinter as tk


def write_history(display,ans):
    """History write.

    Write anser in the text box and save the equation in history file.

    Args:
        ans(str):The answer of the equation
        display(Any): Some function and values about the text of the window
        history_file(TextIOWrapper):The file of history
    """
    display.insert(tk.END,'=')
    display.insert(tk.END,ans)
    ans=display.get(1.0,tk.END)

    history_file=open("history.txt","a")
    history_file.write(ans)
    history_file.close()


def read_history(root):
    """Read history.

    Read the history equations which save in the history files.
    
    Args:
        root(Tk): the window
        history_file(TextIOWrapper):the file of history.
        strs(str):the equtions in the file.
        window_history(Toplevel): a new window used to show the history
        history_eqution(Text):a text box used to show the history on the window
        i(str): a equaiton in the history file
    """
    history_file=open("history.txt","r+")
    strs=history_file.read()
    window_history=tk.Toplevel(root)
    window_history.geometry('300x200')
    window_history.title('history')
    history_eqution=tk.Text(window_history,height=10,undo=True)
    for i in strs:
        history_eqution.insert(tk.END,i)
        print(i)
    history_eqution.pack(side='top')
    history_file.close()
