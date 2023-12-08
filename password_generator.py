import random
print("welcome to password generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['*','!','@','#','$','%','^','&','(',')','-','+']
l = int(input("how many letters you want in your password?\n"))
n = int(input("how many numbers you want in your password?\n"))
s = int(input("how many symbols you want in your password?\n"))
password=""
for i in range(1, l + 1):
    char = random.choice(letters)
    password += char
for j in range(1, n + 1):
    char = random.choice(numbers)
    password += char
for k in range(1, s + 1):
    char = random.choice(symbols)
    password += char
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
# password = ""
# for i in password_list:
#     password += char
print(password)
