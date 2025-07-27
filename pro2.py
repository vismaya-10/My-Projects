import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols =['!','#','$','%','&','(',')','*','+']

print("Welcome to PASSWORD generator")
no_letters=int(input("How many letters would you like in your password?\n"))
no_numbers=int(input("How many numbers do you want?\n"))
no_symbols=int(input("How many symbols would you like?\n"))

password_list=[]

for char in range(0,no_letters):
    password_list.append(random.choice(letters))
for char in range(0,no_numbers):
    password_list.append(random.choice(numbers))
for char in range(0,no_symbols):
    password_list.append(random.choice(symbols))
    
print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+=char
print(f"The final password generated is:{password}")