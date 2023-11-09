while True:

    length=0
    width=0
    length=float(input("enter the length of the floor: "))
    width=float(input("enter the width of the floor: "))
    rate=str(input("enter economy, durable or premium: ")).lower()

    #material cost is area * rate
    area=length*width
    labourcost=120+area*5.25#
    vat=1.22

    if rate=="economy":
        total_1=area*7.99
        print("your total is: ",(total_1+labourcost)*vat)
        
    if rate=="durable":
        total_2=area*12.90
        print("your total is: ",(total_2+labourcost)*vat)
        
    else:
        total_3=area*21.40
        print("your total is: ",(total_3+labourcost)*vat)

        option=input("press n to stop or enter to continue: ").lower()
        if option=="n":
              break
