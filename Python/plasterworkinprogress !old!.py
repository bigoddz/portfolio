#this program calculates how much paint is needed to paint a room

height=0
width1=0
width2=0
door=0
window=0
doorheight=0
doorweidth=0
windowheight=0
windowwidth=0
tincost=12

height=float(input("enter the height of a room: "))
width1=float(input("enter one width of the room: "))
width2=float(input("enter another width of the room: "))

door=int(input("enter the amount of doors in the room: "))
window=int(input("enter the amount of windows in the room: "))

doorheight=float(input("enter the height of each door: "))
doorweidth=float(input("enter the weidth of each door: "))

windowheight=float(input("enter the height of each window: "))
windowweidth=float(input("enter the width of each window: "))

doorarea=doorheight*doorweidth
windowarea=windowheight*windowwidth

area_wall1=height*width1
area_wall2=height*width2
room=area_wall1+area_wall2-doorarea-windowarea

print("your room is a total of: ",room)

tinamount=input("a single tin of (£12) can paint 4sqm^2 how many would you like to order: ")
















