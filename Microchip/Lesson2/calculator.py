a = float(input("Մուտքագրեք առաջին թիվը: "))
b = float(input("Մուտքագրեք երկրորդ թիվը: "))

operation = input("Մուտքագրեք գործողությունը (+, -, *, /): ")

if operation == "+":
    print("Արդյունք =", a + b)
elif operation == "-":
    print("Արդյունք =", a - b)
elif operation == "*":
    print("Արդյունք =", a * b)
elif operation == "/":
    if b != 0:
        print("Արդյունք =", a / b)
    else:
        print("Զրոյի վրա բաժանել չի կարելի։")
else:
    print("Սխալ գործողություն։")
