#BMI with elif and else

print("Disclaimer: BMI is very inaccurate")

weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))

kgperpound = 0.45359237
metersperinch = 0.0254

weightinKG = weight * kgperpound
heightinmeters = height * metersperinch

bmi = weightinKG / (heightinmeters ** 2)

print("BMI is", format(bmi, ".2f"))


if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print(" 'Normal' ")
elif bmi < 30:
    print("Over weight")
else:
    print("Obese")

