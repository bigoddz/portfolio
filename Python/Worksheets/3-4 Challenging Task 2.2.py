weekly=0
overtime=21
total=0

name=str(input("enter your name: "))
hours=float(input("enter the amount of hours worked this week: "))
pay_rate=float(input("enter your hourly pay rate: "))
overtime=float(input("enter the amount of hours worked overtime: "))
               
weekly=hours*pay_rate
overtime=pay_rate*overtime
total=weekly+overtime

overtime

print("Hey",name,"you have earned:£",total,"this week.")
