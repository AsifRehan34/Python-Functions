def BMICalculator(weight,height):
    BMI=(weight/height*height)
    BMIResult(BMI)
def BMIResult(BMI):
    if BMI<=20:
        print("Under weighht")
    elif BMI>20 and BMI<=30:
        print("Perfect")
    else:
        print("Overweight")
number_of_people=int(input("Enter the number of people"))
for i in range(number_of_people):
    weight=int(input("Enter your weight: "))
    height=int(input("Enter your height: "))
    BMICalculator(weight,height)
