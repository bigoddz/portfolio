occupation=float(input("how many years have you worked for this organisation: "))
salary=float(input("what is your current salary: "))

if occupation<5:
    print("you're not eligble for a bonus")

else:
    print("your new salary is: ",salary*1.06)
