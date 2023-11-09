#how can we create an edp application (Event Driven Programming)

#step 1
from tkinter import* # (toolkit interface)

mywindow=Tk()

mywindow.geometry("400x700") #define the size and location
mywindow.title("Terminator") #identify the window

#to put in middle use .pack()
mylabel=Label(mywindow,text="enter number of cars: ",fg="pink",bg="black").grid(row=0,column=0,sticky=W) 
mylabel2=Label(mywindow,text="enter the value of the cars: ",fg="pink",bg="black").grid(row=1,column=0,sticky=W)
mylabel3=Label(mywindow,text="this is my third label ",fg="pink",bg="black").grid(row=2,column=0,sticky=W) 
mylabel4=Label(mywindow,text="this is my four label ",fg="pink",bg="black").grid(row=3,column=0,sticky=W)

mybutton=Button(mywindow,text="OK").grid(row=4,column=1)
mybutton1=Button(mywindow,text="Cancel",command=quit).grid(row=4,column=0,sticky=W)

entry=Entry(mywindow,textvariable="car").grid(row=0,column=1)
entry1=Entry(mywindow,textvariable="carsales").grid(row=1,column=1)
