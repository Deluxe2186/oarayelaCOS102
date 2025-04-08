print("This is a program designed to calculate\n "
"the area of a circle\n"
"kindly follow the instructions below:")
def calculate_area(radius):
    pi = 3.14
    area = pi * radius**2
    print("Radius of the circle is: ", area)
    return
calculate_area(float(input("Enter a value for the radius of the circle:  ")))