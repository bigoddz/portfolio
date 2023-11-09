while True:


     litres=0
     age=0

     litres=float(input("enter your engine's litres: "))
     gender=str(input("enter your gender: "))
     age=float(input("enter your age: "))


     if litres < 1.4:
          annum=429
     elif litres >= 1.4 and litres <= 1.99:
          annum=599
     else:
          annum=779
         
     if age<21:
          extra=3.2
     elif age>=21 and age <25:
          extra=1.75
     else:
          extra=0
     if gender=="male":
          bonus=0.22
     else:
          bonus=0

     cost=annum*extra+annum*bonus+annum
     print("your total is: ",cost)

     option=input("press n to stop or enter to continue: ").lower()
     if option=="n":
               break
