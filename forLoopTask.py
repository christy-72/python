#####

print("question 1")

for x in range(10):
	print(x)

print("")

#####

print("question 2")

for x in range(2, 10):
	print(x)

print("")

####

print("question 3")

for x in range(2, 100, 3):
	print(x)

print("")

####

print("question 4")

for x in range(2, 10, 3):
	print(x)

print("")

####

print("question 5")

for x in range(10):
	print(x)
else:
	print("Finished counting")

print("")

####

print("question 6")

for x in range(10):
	if x == 3: break
	print(x)
else:
	print("Finished counting")

print("")

####

print("question 7")

people= ["Joseph", "Alma", "Siamak"]
for x in people:
	print(x)
	if x == " Siamak":
		break

print("")

####

print("question 8")

people = ["Joseph", "Alma", "Siamak"]
for x in people:
	if x == "Siamak":
		break
	print(x)

print("")

####

print("question 9")

people = ["Joseph", "Alma", "Siamak"]
for x in people:
	if x == " Siamak":
		continue
	print(x)