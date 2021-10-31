import math
from tkinter import messagebox
from tkinter import *
screen=Tk()
screen.configure(bg='blue')
screen.title('mycalculator')
screen.maxsize(width=453,height=488)
screen.minsize(width=362,height=488)

def click(number):
    global operator
    operator+=str(number)
    tex.set(operator)
def clear():
    global operator
    operator=''
    tex.set(operator)
def equal():
    global operator
    try:
      res=eval(operator)
      operator=str(res)
      tex.set(res)
    except:
        messagebox.showinfo('notification','try again something is wrong!!')

def cmsin():
    global operator

    res=math.sin(eval(tex.get()))
    operator=str(res)
    tex.set(res)
def cmcos():
    global operator
    res=math.cos(eval(tex.get()))
    operator=str(res)
    tex.set(res)
def cmtan():
    global operator
    res = math.tan(eval(tex.get()))
    operator = str(res)
    tex.set(res)
def cmsqrt():
    global operator
    res = math.sqrt(eval(tex.get()))
    operator = str(res)
    tex.set(res)
def cmlog():
    global operator
    res = math.log(eval(tex.get()))
    operator = str(res)
    tex.set(res)

tex=StringVar()
operator=''
entry1=Entry(screen,bg='powder blue',justify='right',bd='30',font=('arial',20,'italic bold'),textvariable=tex,)
entry1.grid(row=0, columnspan=4)
btn7= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='7',bd=8,command=lambda :click(7))
btn7.grid(row=1,column=0)
btn8= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='8',bd=8,command=lambda :click(8))
btn8.grid(row=1,column=1)
btn9= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='9',bd=8,command=lambda :click(9))
btn9.grid(row=1,column=2)
btnadd= Button(screen,font=('arial',19,'italic bold'),padx=16,pady=16,text='+',bd=8,command=lambda :click('+'))
btnadd.grid(row=1,column=3)
btn4= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='4',bd=8,command=lambda :click(4))
btn4.grid(row=2,column=0)
btn5= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='5',bd=8,command=lambda :click(5))
btn5.grid(row=2,column=1)
btn6= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='6',bd=8,command=lambda :click(6))
btn6.grid(row=2,column=2)
btnsub= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='-',bd=8,command=lambda :click('-'))
btnsub.grid(row=2,column=3)
btn1= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='1',bd=8,command=lambda :click(1))
btn1.grid(row=3,column=0)
btn2= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='2',bd=8,command=lambda :click(2))
btn2.grid(row=3,column=1)
btn3= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='3',bd=8,command=lambda :click(3))
btn3.grid(row=3,column=2)
btnmul= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='*',bd=8,command=lambda :click('*'))
btnmul.grid(row=3,column=3)
btn0= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='0',bd=8,command=lambda :click(0))
btn0.grid(row=4,column=0)
btnclear= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='C',bd=8,command=clear)
btnclear.grid(row=4,column=1)
btnequal= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='=',bd=8,command=equal)
btnequal.grid(row=4,column=2)
btndiv= Button(screen,font=('arial',21,'italic bold'),padx=16,pady=16,text='/',bd=8,command=lambda :click('/'))
btndiv.grid(row=4,column=3)
btnsin= Button(screen,font=('arial',19,'italic bold'),padx=16,pady=18,text='sin',bd=8,command=cmsin)
btnsin.grid(row=0,column=4)
btnscos= Button(screen,font=('arial',19,'italic bold'),padx=16,pady=18,text='cos',bd=8,command=cmcos)
btnscos.grid(row=1,column=4)
btntan= Button(screen,font=('arial',20,'italic bold'),padx=16,pady=18,text='tan',bd=8,command=cmtan)
btntan.grid(row=2,column=4)
btnsqrt= Button(screen,font=('arial',17,'italic bold'),padx=16,pady=18,text='sqrt',bd=8,command=cmsqrt)
btnsqrt.grid(row=3,column=4)
btnlog= Button(screen,font=('arial',20,'italic bold'),padx=16,pady=18,text='log',bd=8,command=cmlog)
btnlog.grid(row=4,column=4)





screen.mainloop()
