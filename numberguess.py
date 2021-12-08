#guess number

import random
number = random.randint(0, 101)

print("Magic Number Game")
print("Welcome...")

guess = -1

while guess != number:
    guess = eval(input("Enter your guess between 0 - 100: "))
    if guess == number:
        print("Well done!!")
    elif guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")