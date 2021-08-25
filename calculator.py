import decimal
class Calculator():
    def __init__(self):
        self.name=Calculator
        self.formula=input("请输入公式")
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
        if '*' in self.formula_list1:
            i=0
            while i<len(self.formula_list1):
                if self.formula_list1[i]=='*':
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
                print(self.zuihouchuli())
                break

calculator=Calculator()
calculator.main()