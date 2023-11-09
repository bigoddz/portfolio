#this script calculates weather the shape is a square or rectangle

while True:

    length=float(input("enter the length of a shape: "))
    width=float(input("enter the width of a shape: "))

    if length==width:
        print("Your shape is a square")

    else:
        print("Your shape is a rectangle")

    choice=str(input("press 'N' to stop or press enter to continue: ")).upper()
    if choice=='n':
        break
