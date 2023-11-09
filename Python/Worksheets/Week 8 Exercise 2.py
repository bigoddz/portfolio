from tkinter import*

GUI=Tk()
GUI.geometry("500x500")

GUI.title("Sales Commission ")

def salary():
    a=float(car.get())
    b=float(sales.get())

    if b<80000:
        commission=0.015
      
    elif b>=80000 and b<=175000:
        commission=0.0225
         
    else:
        commission=0.0279
    total=(a*129)+(b*commission)
    result=Label(GUI,text="the salary that will be allocated is £ %.2f"%total).grid(row=3,column=0)  
    
car=StringVar()
sales=StringVar()

label1=Label(GUI,text="Input Number of Cars ").grid(row=0,column=0)

mybox=Entry(GUI, textvariable=car).grid(row=0,column=1)

label2=Label(GUI, text="Input Sales Value ").grid(row=1,column=0)

mybox=Entry(GUI, textvariable=sales).grid(row=1,column=1)

button1=Button(GUI, text="Calculate ",command=salary).grid(row=2,column=0)
button2=Button(GUI, text="Exit",command=quit).grid(row=2, column=1)
