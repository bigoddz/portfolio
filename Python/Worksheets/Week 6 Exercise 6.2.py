import random

def report_random():
    my_number=random.randint(20,100)
    return my_number

#main program
a=report_random() #return a random int and assign it to a
print("a is equal to ",a)
b=report_random()
print("b is equal to ",b)
c=report_random()
print("c is equal to ",c)
