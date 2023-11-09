while True:
    length=float(input("enter the length of the room: "))
    width=float(input("enter the width of the room: "))
    height=float(input("enter the height of the room: "))
    decor=str(input("enter if you want paint or wallpaper: ")).lower()

    area=length*height*2+width*height*2
    labour_wall=(77.80+area*2.29)*1.22
    labour_paint=(77.80+area*1.34)*1.22

    if decor=="paint":
       print("your total is: ",labour_paint)
    else:
    print("your total is: ",labour_wall)

    option=input("press n to stop or enter to continue: ").lower()
         if option=="n":
              break
