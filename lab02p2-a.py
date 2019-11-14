import math

def check_if_valid():
    while True:
        try:
            val = float(input("Please enter a number: "))
        except ValueError:
            print("That is not a number. Please try again.")
        else:
            return val

def circ(a):
    return a*math.pi

def area_circle(a):
    return ((a/2)**2)*math.pi

x = check_if_valid()

print("Circumference of the circle: " + str(circ(x)))
print("Area of a circle: " + str(area_circle(x)))