#%%
import tkinter as tk
from tkinter.constants import DISABLED, END, INSERT, S
from typing import Text

def command_1():
    display.insert(tk.END,'1')

def command_2():
    display.insert(tk.END,'2')

def command_3():
    display.insert(tk.END,'3')

def command_4():
    display.insert(tk.END,'4')

def command_5():
    display.insert(tk.END,'5')

def command_6():
    display.insert(tk.END,'6')

def command_7():
    display.insert(tk.END,'7')

def command_8():
    display.insert(tk.END,'8')

def command_9():
    display.insert(tk.END,'9')

def command_bracket_l():
    display.insert(tk.END,'(')

def command_bracket_r():
    display.insert(tk.END,')')

def command_C():
    display.delete(1.0,tk.END)

def command_division():
    display.insert(tk.END,'/')

def command_multi():
    display.insert(tk.END,'x')

def command_delete():
    display.edit_undo()

def command_sbustraction():
    display.insert(tk.END,'-')

def command_addion():
    display.insert(tk.END,'+')

def command_equal():
    equation=display.get(1.0,tk.END)
    calculator=Calculator(equation)
    calculator.main()
    
def command_0():
    display.insert(tk.END,'0')

def command_dot():
    display.insert(tk.END,'.')

def command_history():
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


def command_readme():
    window_help=tk.Toplevel(root)
    window_help.geometry('300x200')
    window_help.title('help')
    label_readme=tk.Label(window_help,text='Readme')
    label_email=tk.Label(window_help,text='luoyeyizhan@163.com')
    label_readme.pack()
    label_email.pack()

class Number:
    def __init__(self,master):
        keyboard=tk.Frame(master)
        keyboard.pack(side='bottom')

        self.button_C=tk.Button(keyboard,text='C',width=10,height=4,command=command_C)
        self.button_C.grid(row=1,column=1)

        self.button_division=tk.Button(keyboard,text='÷',width=10,height=4,command=command_division)
        self.button_division.grid(row=1,column=2)

        self.button_multiplication=tk.Button(keyboard,text='x',width=10,height=4,command=command_multi)
        self.button_multiplication.grid(row=1,column=3)

        self.button_delete=tk.Button(keyboard,text='backout',width=10,height=4,command=command_delete)
        self.button_delete.grid(row=1,column=4)

        self.button1=tk.Button(keyboard,text='1',width=10,height=4,command=command_1)
        self.button1.grid(row=2,column=1)

        self.button2=tk.Button(keyboard,text='2',width=10,height=4,command=command_2)
        self.button2.grid(row=2,column=2)

        self.button3=tk.Button(keyboard,text='3',width=10,height=4,command=command_3)
        self.button3.grid(row=2,column=3)

        self.button4=tk.Button(keyboard,text='4',width=10,height=4,command=command_4)
        self.button4.grid(row=3,column=1)

        self.button5=tk.Button(keyboard,text='5',width=10,height=4,command=command_5)
        self.button5.grid(row=3,column=2)

        self.button6=tk.Button(keyboard,text='6',width=10,height=4,command=command_6)
        self.button6.grid(row=3,column=3)

        self.button7=tk.Button(keyboard,text='7',width=10,height=4,command=command_7)
        self.button7.grid(row=4,column=1)

        self.button8=tk.Button(keyboard,text='8',width=10,height=4,command=command_8)
        self.button8.grid(row=4,column=2)

        self.button9=tk.Button(keyboard,text='9',width=10,height=4,command=command_9)
        self.button9.grid(row=4,column=3)

        self.bracket_l=tk.Button(keyboard,text='(',width=10,height=4,command=command_bracket_l)
        self.bracket_l.grid(row=5,column=1)

        self.button0=tk.Button(keyboard,text='0',width=10,height=4,command=command_0)
        self.button0.grid(row=5,column=2)

        self.button_bracket_r=tk.Button(keyboard,text=')',width=10,height=4,command=command_bracket_r)
        self.button_bracket_r.grid(row=5,column=3)

        self.button_substraction=tk.Button(keyboard,text='-',width=10,height=4,command=command_sbustraction)
        self.button_substraction.grid(row=2,column=4)

        self.button_addtion=tk.Button(keyboard,text='+',width=10,height=4,command=command_addion)
        self.button_addtion.grid(row=3,column=4)
        
        self.button_equal=tk.Button(keyboard,text='=',width=10,height=4,command=command_equal)
        self.button_equal.grid(row=4,column=4)

        self.button_dot=tk.Button(keyboard,text='.',width=10,height=4,command=command_dot)
        self.button_dot.grid(row=5,column=4)

import decimal
class Calculator():
    def __init__(self,equation):
        self.name=Calculator
        self.formula=equation
        print(equation)
        self.formula_list1=[]
        self.formula_list2=[]
    
    def zhuanhuan(self):
        sum=''
        num=0
        while num<len(self.formula_list1):#num最大为列表长度减1，因为列表遍历从零开始
            if self.formula_list1[num].isdigit() or self.formula_list1[num]=='.':#若self.formula_list1[num]为数字
               sum+=self.formula_list1[num]#这样sum最终会存储一个数字
               num+=1
               if num==len(self.formula_list1):#此时num已经超出列表遍历
                    buc=len(sum)
                    self.formula_list1[(num-buc):num]=[sum]
                    

            else:
                buc=len(sum)
                self.formula_list1[(num-buc):num]=[sum]#将列表中num-buc到num-1的元素替换成了sum，此时数字只占一格
                sum=''#遇见符号，清空sum
                num=num+1-(buc-1)
        for word in self.formula_list1:
            if word=='':
                self.formula_list1.remove(word)       

    def chengfa(self):
        if 'x' in self.formula_list1:
            i=0
            while i<len(self.formula_list1):
                if self.formula_list1[i]=='x':
                    for word in self.formula_list1:
                        if word=='':
                            self.formula_list1.remove(word)
                    sum=decimal.Decimal(self.formula_list1[i-1])*decimal.Decimal(self.formula_list1[i+1])
                    self.formula_list1[(i-1):(i+2)]=[str(sum)]
                    i=i-2
                else:
                    i=i+1
            
    def chufa(self):
        if '/' in self.formula_list1:
            i=0
            #print(self.formula_list1)
            while i<len(self.formula_list1):
                if self.formula_list1[i]=='/':
                    for word in self.formula_list1:
                        if word=='':
                            self.formula_list1.remove(word)
                    sum=decimal.Decimal(self.formula_list1[i-1])/decimal.Decimal(self.formula_list1[i+1])
                    self.formula_list1[(i-1):(i+2)]=[str(sum)]
                    i=i-2
                else:
                    i=i+1
            
    def jianfa(self):
        if '-' in self.formula_list1:
            i=0
            while i<len(self.formula_list1):
                if self.formula_list1[i]=='-':
                    for word in self.formula_list1:
                        if word=='':
                            self.formula_list1.remove(word)
                    sum=decimal.Decimal(self.formula_list1[i-1])-decimal.Decimal(self.formula_list1[i+1])
                    self.formula_list1[(i-1):(i+2)]=[str(sum)]
                    i=i-2
                else:
                    i=i+1

    def zuihouchuli(self):        
        self.chufa()
        self.chengfa()   
        self.jianfa()#此时只剩加法
        if '+' in self.formula_list1:
            result=0
            for number in self.formula_list1:
                if number.isdigit() or '.' in number:
                    result+=decimal.Decimal(number)
            return(str(result))
        else:
            return(str(self.formula_list1[0]))

    def main(self):
        self.formula_list1=list(self.formula)
        self.zhuanhuan()
        num=0
        sum=[]
        while num<len(self.formula_list1):
            while '('  in self.formula_list1 and num<len(self.formula_list1):
                if self.formula_list1[num]==')'  and self.formula_list1[num-1].isdigit():
                    num1=num-1
                    while self.formula_list1[num1]!='(':
                        sum.append(self.formula_list1[num1])
                        num1-=1
                    else:#此时self.formula_list1[num1]='('
                        self.formula_list2=self.formula_list1                      
                        self.formula_list1=list(reversed(sum))#翻转，因为之前是倒着加的所以要翻转一下
                        suan=self.zuihouchuli()#计算括号中的式子
                        self.formula_list2[num1:num+1]=[suan]#将括号带括号内数字整个变为结果
                        self.formula_list1=self.formula_list2
                        self.formula_list2=[]
                        sum=[]
                        num=0#重新遍历
                else:
                    num+=1
            else:
                display.insert(tk.END,'=')
                ans=self.zuihouchuli()
                display.insert(tk.END,ans)
                ans=display.get(1.0,tk.END)
                history_file=open("history.txt","a")
                history_file.write(ans)
                history_file.close
                break

class cal_menu:
    def __init__(self,master):
        menubar=tk.Menu(master)

        filemenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='File',menu=filemenu)
        filemenu.add_command(label='New',command=command_C)
        filemenu.add_command(label='history',command=command_history)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',command=master.quit)

        helpmenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='help',menu=helpmenu)
        helpmenu.add_command(label='getback',command=command_delete)
        helpmenu.add_command(label='readme',command=command_readme)

        master.config(menu=menubar)

        

root=tk.Tk(className='calculator')
root.geometry('330x480')
display=tk.Text(root,width=330,height=5,undo=True)
display.pack(side='top')
Number(root)
cal_menu(root)
root.mainloop()

# %%
