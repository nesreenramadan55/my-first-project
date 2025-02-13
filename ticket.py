age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 5
elif age <= 59:
    price = 10
else:
    price = 7

print(f"The ticket price is ${price}.")