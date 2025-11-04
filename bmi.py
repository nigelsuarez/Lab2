def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    myBMI = weight/(height*height)
    myValue = 0

    print("BMI: " + str(myBMI))

    if myBMI < 18.5:
        print("Under Weight")
        myValue = -1
    elif (myBMI >= 18.5) and (myBMI <= 25.0):
        print("Normal Weight")
        myValue = 0
    elif myBMI > 25.0:
        print("Over Weight")
        myValue = 1

    return myValue

print(calculate_bmi(weight=70, height=1.70))