# asking user what type of equation they want to solve
eqn = ["Quadratic", "Cubic", "Quartic"]
print("What type of equation do you want to solve?")
print("1. Quadratic equation")
print("2. Cubic equation")
print("3. Quartic equation")
choice = int(input("Enter your choice: "))
print(f"you have chosen {eqn[choice-1]} equation")
if choice == 1:
    a = float(input('Enter a value for the coefficient of X^2'))
    b = float(input('Enter a value for the coefficient of X'))
    c = float(input('Enter a value for the constant'))
    d = (b**2) - (4*a*c)
    if d < 0:
        print("No real roots")
    elif d == 0:
        x = (-b) / (2*a)
        print(f"the root is {x}")
    else:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        print(f"the roots are {x1} and {x2}")
elif choice != 1:
    print("This equation is not supported yet")