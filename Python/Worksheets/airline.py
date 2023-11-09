while True:

    print("welcome to xyz airlines")
    print("the number of tickets available are 152")
    print("the price of adult seats will cost £120")
    print("the price of child seats will cost £60")

    adult_seat=input("enter the number of adult seats required: ")
    child_seat=input("enter the number of child seats required: ")

    adult_price=adult_seat*120
    child_price=child_seat*60
    total=adult_price+child_price

if total<=152:
    print("your total is: ",total)



