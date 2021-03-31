#bmimetric2
weight = float(input("please enter weight in kilograms: "))
height = float(input("please enter height in meters: "))
bmi = round(weight / height**2, 2)

if(bmi<18.5):
    status = "Underweight"
elif(18.5<=bmi<25):
    status = "Normal"
elif(25<=bmi<30):
    status = "Overweight"
else: 
    status = "Obese"
    
print("BMI is: ", bmi,", Status is ", status, sep=(""))

