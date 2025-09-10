import random

Random_guess = random.randint(1,10)

while True:
    print("Your Guessed number is :",Random_guess)
    result = input("Press Y if it is correct or N if it is worng:")

    if result == "Y":
        print("I Guessed you")
        break

    else:
        continue