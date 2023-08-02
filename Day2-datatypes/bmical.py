# Developed by: Victor Chiemeka
# Date: 2/08/2023
# Description: This program is a BMI Calculator

# Bmi calculator
weight = int(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))

bmi = weight / (height ** 2)
bmi_int = int(bmi)
print("Your BMI is:", bmi_int)
