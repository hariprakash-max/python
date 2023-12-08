size = input("what size pizza you want(S/M/L/U)? ")
bill = 0
if size == 'S' or size == 's':
    bill += 100
    print("Small pizza price is 100 Rs.")
elif size == 'M' or size == 'm':
    bill += 200
    print("Medium Pizza price is 200 Rs.")
elif size == 'L' or size == 'l':
    bill += 250
    print("Large pizza price is 250 Rs.")
else:
    bill += 300
    print("Ultra pizza price is 300 Rs.")

add_pepper = input("Do you want pepper(Y/N)? ")
if add_pepper == 'Y' or add_pepper == 'y':
    if size == 'S' or size == 's':
        bill += 300
    else:
        bill += 50
extra_cheese = input("Do you want extra cheese(Y/N)? ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 20

print(f"your final bill is {bill}")
