def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

y = []
def get_user_input():
    userData = input('Enter numbers: ')
    x = userData.split(",")

    for i in x:
        y.append(float(i))
    print(y)

def calc_average_temperature():
    x = 0
    for i in y:
        x = x + i
    calcAVGtemp = x/len(y)
    print(calcAVGtemp)


def find_min_max():
    print(min(y))
    print(max(y))

def sort_temperature():
    print(sorted(y))

def calc_median_temperature():
    median = 0
    x = len(sorted(y))/2

    if len(y) % 2:
        median = sorted(y)[int(x)]
    else:
        median = (sorted(y)[int(x)] + sorted(y)[int(x)-1])/2

    print(median)

def test():
    thislist = ["apple", "banana", "cherry"]
    print(thislist)

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    myBMI = weight/(height*height)

    print("BMI: " + str(myBMI))

    if myBMI < 18.5:
        print("Under Weight")
    elif (myBMI >= 18.5) and (myBMI <= 25.0):
        print("Normal Weight")
    elif myBMI > 25.0:
        print("Over Weight")

if __name__ == "__main__":
    main()