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

def calc_average_temperature(j):
    x = 0
    for i in j:
        x = x + i
    calcAVGtemp = x/len(j)
    print(calcAVGtemp)

    return calcAVGtemp


def find_min_max(j):
    minNum = min(j)
    maxNum = max(j)

    return [minNum, maxNum]

def sort_temperature():
    print(sorted(y))

def calc_median_temperature(j):
    median = 0
    x = len(sorted(j))/2

    if len(j) % 2:
        median = sorted(j)[int(x)]
    else:
        median = (sorted(j)[int(x)] + sorted(j)[int(x)-1])/2

    print(median)

    return median

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