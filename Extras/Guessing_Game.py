import random

random_picker = random.randint(1,5)

print("Guess a number Between 1 to 10")

while True:
    guess = int(input("Enter the guessed number:"))

    if guess == random_picker:
        print("Your guess is correct!")
        break

    else:
        print("Wrong try again")