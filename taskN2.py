# 1
print("Age Verification")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.\n")
else:
    print("You are a minor.\n")
# 2
    print("Number Sign Determination")
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.\n")
elif num < 0:
    print("The number is negative.\n")
else:
    print("The number is equal to zero.\n")

    print("--- Mini Calculator ---")
num1 = float(input("Enter the first number: "))
op = input("Choose an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
# 3
if op == '+':
    print(f"Result: {num1 + num2}")
elif op == '-':
    print(f"Result: {num1 - num2}")
elif op == '*':
    print(f"Result: {num1 * num2}")
elif op == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero.")
else:
    print("Unknown mathematical operation.")
