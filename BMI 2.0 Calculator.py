height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi=weight/(height**2)
print(f"The BMI is : {bmi:.2f}.",end="")
if bmi < 18.5:
    print(" You are underweight")
elif bmi < 25:
    print(" You are normal weight")
elif bmi < 25:
    print(" You are normal weight")
elif bmi < 30:
    print(" You are over weight")
elif bmi < 35:
    print(" You are obese")
else:
    print("You are clinically obese")