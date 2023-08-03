# Developed by: Victor Chiemeka
# Date: 3/08/2023
# Description: This program is a BMI Calculator

# Bmi calculator
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))


bmi_int = round(weight / (height ** 2))
if bmi_int <= 18.5:
    print(f"Your BMI is {bmi_int},you are underweight")

elif (bmi_int <= 25):
    print(f"Your BMI is {bmi_int}, You have a normal weight")

elif (bmi_int <= 30):
    print(f"Your BMI is {bmi_int},You are overweight")

elif (bmi_int <= 35):
    print(f"Your BMI is {bmi_int},You are obese")

else:
    print(f"Your BMI is {bmi_int},you are technically obese")
