def check_if_num():
    while True:
        try:
            val = float(input("Please enter a number: "))
        except ValueError:
            print("This is not a number. Please try again.")
        else:
            return float(val)

def perimeter(a,b):
    return 2*(a+b)

def area(a,b):
    return a*b

x = check_if_num()
y = check_if_num()

print("The perimeter of your shape is: " + str(perimeter(x,y)))
print("The area of your shape is: " + str(area(x,y)))