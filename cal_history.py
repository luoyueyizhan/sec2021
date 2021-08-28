import tkinter as tk


def write_history(display,ans):
    display.insert(tk.END,'=')
    display.insert(tk.END,ans)
    ans=display.get(1.0,tk.END)

    history_file=open("history.txt","a")
    history_file.write(ans)
    history_file.close()


def read_history(root):
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
