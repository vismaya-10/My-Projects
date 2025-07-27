print("Welcome to the rollercoaster ride")
height=int(input("enter your height"))
bill=0

if(height>120):
    print("welcome to the rollercoaster ride")
    age=int(input("enter age"))
    if(age<=12):
        bill=5
        print("the ticket is 5$")
        
    elif(age<=18):
        bill=7
        print("the ticket is $7")
        
    elif(age>=45 and age<=55): #   45<=age =<55
        print("you get to ride free")
        
    else:
        bill=12
        print("the ticket is 12$")
        
    want_photo=input("type y for yes or no for n")
    if(want_photo== "y"):
        bill+=3
        print(f"the final bill is{bill}")
else:
    print("sorry better luck next timeS")
        