print("\n--- Loops Demo ---")

#1
print("Numbers from 1 to 100 divisible by 5:")
for i in range(1, 101):
    if i % 5 == 0:
        print(i, end=" ")
print("\n")


# 2
N = int(input("Enter number N for sum calculation: "))
total_sum = 0
for i in range(1, N + 1):
    total_sum += i
print(f"The sum of numbers from 1 to {N} is: {total_sum}\n")


# 3
print("--- Guess the Number Game ---")
secret_number = 37
guess = 0

print("The system has chosen a number between 1 and 50.")

while guess != secret_number:
    guess = int(input("Guess the number: "))
    if guess < secret_number:
        print("Enter a higher number.")
    elif guess > secret_number:
        print("Enter a lower number.")
    else:
        print("Congratulations, you guessed the correct number!")
