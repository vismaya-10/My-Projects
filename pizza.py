print("welcome to th pizza delievery")
size=input("what size do you want?S,M or L:")
pepporini=input("Do you want pepporini pizza?Y or N:")
extra_cheese=input("Do you want extra cheese?Y or N:")
bill=0
if(size=="S"):
    bill+=15
    print("the cost is $15")
elif(size=="M"):
    bill+=20
    print("the cost is $20")
elif(size=="L"):
    bill+=25
    print("the cost is 25")
else:
    print("typed wronf inputs")
if pepporini =="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese =="Y":
    bill+=1
print(f"the final bill is {bill}:")
        