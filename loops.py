## LOOPS

#for loop

my_fruit = ["Apple", "Banana", "Orange"]

for fruit in my_fruit:
    print(fruit.upper())

for number in range(5):
    print(number)


for char in "Hello world":
    print(char)
for word in "Hello world".split():
    print(word)



diction = {"key": "value"}

for key in {"key": "value"}:
    print(key)
for value in {"key": "value"}.values():
    print(value)

for key, value in diction.items():
    print(key, value)

print("\n")



result = []
for x in range(5):
    result.append(x)
    print(result)


print([x for x in range(5)])


for i in range(10):
    print(i)
    if i == 5:
        break

for i in range(10):
    if i == 5:
        break
    print(i)

#skips 5:
for i in range(10):
    if 1 == 5:
        continue
    print(i)



for i in range(3):
    for j in range(4):
        print(i, "x", j, "=", i * j)


for i in range(5, 11):
    print(i)
