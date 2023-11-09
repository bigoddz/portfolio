from tkinter import*

GUI=Tk()
GUI.geometry("500x500")

GUI.title("Plaster Application ")

def cost():
    a=float(length.get())
    b=float(width.get())
    c=float(height.get())
    d=str(decor.get())
    if decor=="paint":
        price=55.90
        costpersq=1.34

    else:
        price=77.90
        costpersq=2.29

    area=a*c*2+b*c*2
    vat=1.22
    total=price+((area*costpersq)*vat)
    result=Label(GUI,text="your total for your room is £ %.2f"%total).grid(row=5,column=0)  
    
length=StringVar()
width=StringVar()
height=StringVar()
decor=StringVar()

label1=Label(GUI,text="enter the length of the room: ").grid(row=0,column=0)

mybox=Entry(GUI, textvariable=length).grid(row=0,column=1)

label2=Label(GUI, text="enter the width of the room: ").grid(row=1,column=0)

mybox=Entry(GUI, textvariable=width).grid(row=1,column=1)

label2=Label(GUI, text="enter the height of the room: ").grid(row=2,column=0)

mybox=Entry(GUI, textvariable=height).grid(row=2,column=1)

label2=Label(GUI, text="enter if you want paint or wallpaper: ").grid(row=3,column=0)

mybox=Entry(GUI, textvariable=decor).grid(row=3,column=1)

button1=Button(GUI, text="Calculate ",command=cost).grid(row=4,column=0)
button2=Button(GUI, text="Exit",command=quit).grid(row=4, column=1)
