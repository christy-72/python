## FUNCTIONS

#procedure:

def greet(firstname, lastname):
    print(f"Hello {firstname} {lastname}")

greet("Steve", "Rogers")

## this is knows as a procedure 
## procedure: performs a specific task when called, not a value (it doesn't return information)
## function: returns one value when executed i.e. outputs information - return value. input() and print() shouldn't be used in functions


#function:

def greet2(firstname, lastname):
    return f"Hello {firstname} {lastname}"

print(greet2("Steve", "Rogers"))


## procedure2:

def greet():
    name = input("What is your name? ")
    print(f"Hello {name}")

greet()

## function2:

def greet(name):
    return f"Hello {name}"

name = input("What is your name? ")
greet(name)


## Default values 

def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

greetingfromme = print(greet("Billy", greeting="Yo"))

print(greetingfromme)


####

def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)
print(added_number*100/50**2)