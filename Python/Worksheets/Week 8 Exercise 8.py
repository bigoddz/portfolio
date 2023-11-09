from tkinter import*
def mhello():
    mtext=ment.get()
    mlabel2=Label(msgui,text=mtext).pack()
    return

msgui=Tk()
ment=StringVar()

msgui.geometry("450x450+300+300")
msgui.title("Terminator 2.0")
mlabel=Label(text="My Label").pack()
mbutton=Button(msgui,text="OK",command=mhello).pack()
mEntry=Entry(msgui,textvariable=ment).pack()

#Menu Construction

menubar=Menu(msgui)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save As")
filemenu.add_command(label="Close")
menubar.add_cascade(label="File",menu=filemenu)
msgui.config(menu=menubar)
