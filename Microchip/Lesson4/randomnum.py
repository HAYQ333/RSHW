import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Գուշակիր թիվը (1-100): "))

    if guess < secret_number:
        print("Քո մուտքագրած թիվը փոքր է։")
    elif guess > secret_number:
        print("Քո մուտքագրած թիվը մեծ է։")
    else:
        print("Շնորհավորում եմ։ Դու գուշակեցիր թիվը։")
        break
