def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    get_user_input()
    calc_average_temperature()
    find_min_max()
    sort_temperature()
    calc_median_temperature()

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
        median = (x + (x+1))/2
    else:
        median = (x + (x+1))/2

    print(median)

def test():
    thislist = ["apple", "banana", "cherry"]
    print(thislist)

if __name__ == "__main__":
    main()