def calculateBMI(height, weight):
    print("Height = " + str(height) )
    print("Weight = " + str(weight) )

def BMIcalculator(height, weight):
    bmi = weight/(height*height)
    print("BMI: "+ str(bmi))

    if bmi < 18.5:
        print("BMI Range: Under Weight")
    elif bmi < 25.0:
        print("BMI Range: Normal Weight")
    elif bmi > 25.0:
        print("BMI Range: Over Weight")

    return bmi


calculateBMI(weight=57, height=1.73)

BMIcalculator(weight=57,height=1.73)
