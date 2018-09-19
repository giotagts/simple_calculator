

from tkinter import*

cal=Tk()
cal.geometry("354x460")
cal.title("My Calcie")
calLabel=Label(cal, text="Calculator", font=("Comic Sans Ms", 30,'bold'))
calLabel.pack(side=TOP)

textin=StringVar()
operator=""

def clickbut(numbers):
    global operator
    operator+=str(numbers)
    textin.set(operator)

def equlbut():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator=''

def equlbut():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator=''

def equlbut():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator=''
    
def equlbut():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator=''

def clrbut():
    textin.set('')

caltext=Entry(cal, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='plum')
caltext.pack()

but1=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut(1),text="1", font=("Courier New", 16, 'bold'))
but1.place(x=10,y=100)
but2=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut(2),text="2", font=("Courier New", 16, 'bold'))
but2.place(x=75,y=100)
but3=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut(3),text="3", font=("Courier New", 16, 'bold'))
but3.place(x=140,y=100)
but4=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut(4),text="4", font=("Courier New", 16, 'bold'))
but4.place(x=10,y=170)
but5=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut(5),text="5", font=("Courier New", 16, 'bold'))
but5.place(x=75,y=170)
but6=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut(6),text="6", font=("Courier New", 16, 'bold'))
but6.place(x=140,y=170)
but7=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut(7),text="7", font=("Courier New", 16, 'bold'))
but7.place(x=10,y=240)
but8=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut(8),text="8", font=("Courier New", 16, 'bold'))
but8.place(x=75,y=240)
but9=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut(9),text="9", font=("Courier New", 16, 'bold'))
but9.place(x=140,y=240)
but0=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut(0),text="0", font=("Courier New", 16, 'bold'))
but0.place(x=10,y=310)
butdot=Button(cal, padx=47, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut("."),text=".", font=("Courier New", 16, 'bold'))
butdot.place(x=75,y=310)
butadd=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut("+"),text="+", font=("Courier New", 16, 'bold'))
butadd.place(x=205,y=100)
butsub=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut("-"),text="-", font=("Courier New", 16, 'bold'))
butsub.place(x=205,y=170)
butmul=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut("*"),text="*", font=("Courier New", 16, 'bold'))
butmul.place(x=205,y=240)
butdiv=Button(cal, padx=14, pady=14, bd=4, bg='medium turquoise', command=lambda:clickbut("/"),text="/", font=("Courier New", 16, 'bold'))
butdiv.place(x=205,y=310)
butclear=Button(cal, pady=119, padx=14, bd=4, bg='medium turquoise', command=clrbut,text="CE", font=("Courier New", 16, 'bold'))
butclear.place(x=270,y=100)
butequal=Button(cal, padx=151, pady=14, bd=4, bg='medium turquoise', command=equlbut,text="=", font=("Courier New", 16, 'bold'))
butequal.place(x=10,y=380)


    
