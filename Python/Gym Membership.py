
membership=str(input("you have three options of memberships to pick from,gold,sliver and bronze: ")).lower()
peak=str(input("what time will the customer prefer, peak or offpeak: ")).lower()
pay=str(input("what will the customer prefer paying annually or monthly: ")).lower()



if membership=="gold" and peak=='peak':
    fee=1800
    total=fee*1.20
    print("your total is: ",total) 

elif membership=='gold' and peak=='offpeak':
    fee=1500
    total=fee*1.20
    print("your total is: ",total)

elif membership=='silver' and peak=='peak':
    fee=900
    total=fee*1.20
    print("your total is: ",total)

elif membership=='silver' and peak=='offpeak':
    fee=700
    total=fee*1.20
    print("your total is: ",total)

elif membership=='bronze' and peak=='peak':
    fee=600
    total=fee*1.20
    print("your total is: ",total)

else:
    fee=500
    total=fee*1.20
    print("your total is: ",total)
        
    
    
