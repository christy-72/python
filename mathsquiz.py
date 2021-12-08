#addition quiz

import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

answer = eval(input(f"What is {number1} + {number2} ? "))

print(f"{number1} + {number2} = {number1 + number2}")


#subtraction quiz

number3 = random.randint(0, 9)
number4 = random.randint(0, 9)

if number3 < number4:
    number3, number4 = number4, number3

answer = eval(input(f"What is {number3} - {number4}? "))

if number3 - number4 == answer:
    print("Well done!")
else:
    print("Incorrect :(")


#Subtraction quiz 2

import random

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input(f"What is {number1} - {number2} "))

while number1 - number2 != answer:
    answer = eval(input(f"Sorry, try again. What is {number1} - {number2} "))

print("well done")