mileage=int(input("type the mileage travelled today: "))
days=int(input("type the amount of days spent with rental: "))
total=39.77*days
tax=1.22


if mileage >= 120 and mileage <= 199:
    sum1=total*1.20
     print("the cost of this rental is: ",sum1*tax)
elif mileage >= 200 and mileage <= 349:
    sum2=total*1.30
     print("the cost of this rental is: ",sum2*tax)
else:
    sum3=total*1.60
     print("the cost of this rental is: ",sum3*tax)
