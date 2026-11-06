# 1
print ("Introduction")

name = input("YOUR NAME")
age = input("YOUR AGE")
city = input("YOUR CITY")

print(f"HELLO, {name}! We are glad to see you from {city}. You are {age} years old.\n")

# 2

print("Mathematical Operations")
a = float(input("Enter number a: "))
b = float(input("Enter number b: "))

print(f"Sum (a + b) = {a + b}")
print(f"Difference (a - b) = {a - b}")
print(f"Product (a * b) = {a * b}")

if b != 0:
    print(f"Quotient (a / b) = {a / b}")
else:
    print("Division by zero is not possible.")
