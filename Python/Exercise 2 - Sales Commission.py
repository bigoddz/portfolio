#this program will calculate car dealership salesman commission
cars=int(input("enter the amount of cars sold: "))
sales=float(input("enter the cost of sales: "))

if sales < 80000.00:
     commission=0.015
  
elif sales >= 80000 and sales <= 175000:
     commission=0.0225
     
else:
    commission=0.0279
 
total=(cars*129)+sales*commission
print("the commission earned this month is: ",total)

