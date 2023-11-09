from tkinter import*

x=Tk()

x.geometry("300x400+400+400")
x.title("Calculator")

text_entry=StringVar()
op=""

Tops=Frame(x, width=300,height=20,bd=4,relief="raise")
Tops.pack(side=TOP)

Below=Frame(x,width=300,height=300,bd=4,relief="raise")
Below.pack(side=BOTTOM)

def Clear(x):
    global op
    op=""
    text_entry.set("")
    return

def Equal(x):
    global op
    sumup=str(eval(op))
    op=""
    text_entry.set(sumup)
    return

def Click(x):
    global op
    op=op+str(x)
    text_entry.set(op)

txtDisplay=Entry(Tops,textvariable=text_entry,font=("arial",18,"bold"),width=21,bd=4, justify="right")
txtDisplay.grid(row=0,column=0)

btc=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="C",command=lambda:Clear("C")).grid(row=4,column=0)
bt0=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="0",command=lambda:Click(0)).grid(row=4,column=1)
btd=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text=".",command=lambda:Click(".")).grid(row=4,column=2)
bte=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="=",command=lambda:Equal("=")).grid(row=4,column=3)

bt1=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="1",command=lambda:Click(1)).grid(row=3,column=0)
bt2=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="2",command=lambda:Click(2)).grid(row=3,column=1)
bt3=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="3",command=lambda:Click(3)).grid(row=3,column=2)
btp=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="+",command=lambda:Click("+")).grid(row=3,column=3)

bt4=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="4",command=lambda:Click(4)).grid(row=2,column=0)
bt5=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="5",command=lambda:Click(5)).grid(row=2,column=1)
bt6=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="6",command=lambda:Click(6)).grid(row=2,column=2)
btn=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="-",command=lambda:Click("-")).grid(row=2,column=3)

bt7=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="7",command=lambda:Click(7)).grid(row=0,column=0)
bt8=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="8",command=lambda:Click(8)).grid(row=0,column=1)
bt9=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="9",command=lambda:Click(9)).grid(row=0,column=2)
btm=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="x",command=lambda:Click("*")).grid(row=0,column=3)

btd=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="÷",command=lambda:Click("/")).grid(row=5,column=0)
btp=Button(Below, padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),width=2,height=2,text="%",command=lambda:Click("%")).grid(row=5,column=1)
