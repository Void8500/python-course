Weight = float(input("What is your weight? "))
Height = float(input("What is your height in meters? "))

BMI = Weight / Height ** 2
print(f"Your BMI is {BMI}")
if BMI < 18.5:
    print("You are underweight.")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are at a healthy weight.")
elif BMI >= 25 and BMI <= 29.9:
    print("You are overweight")
elif BMI >= 30 and BMI <= 34.9:
    print("You are obese")
elif BMI >= 35 and BMI <= 39.9:
    print("You are severely obese")
else:
    print("You are morbidly obese.")