#Boolean variable 

my_boolean = False

if my_boolean:
    print("My boolean is truthy")
else:
    print("This is not the truth")

print("\n")


#money

money = 10

if money >= 10:
    print("Rich guy")
else:
    print("poor man")

print("\n")


#deposit

deposit = 10 
password = "password"

if 0 < deposit <= 100 and password == "password":
    print("Thansk for the deposit of", deposit)
else:
    print("This is not valid")

print("\n")


#name

name = "Billy"

if name not in ("root", "admin"):
    print(f"Welcome {name}")
else:
    print("This username is not valid")

print("\n")


#age

age = int(input("Enter age: "))

if age >= 85:
    print("You are above 85")
elif age >= 50:
    print("you are between 50 and 85")
else:
    print("you are below 50")