#Write a Python program that takes a person's height (in meters)
#and weight (in kilograms) as input and calculates their Body Mass Index (BMI).
#Print out their BMI and a message indicating whether they are underweight
#(<18.5), normal (18.5-24.9), overweight (25-29.9), or obese (>=30).

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print("Your BMI is", bmi)
if bmi>=30:
    print("You are obese")
elif bmi>=25:
    print("You are overweight")
elif bmi>=18.5:
    print("You are normal")
else:
    print("You are underweight")