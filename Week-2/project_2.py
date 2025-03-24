# asking user what type of equation they want to solve
eqn = ["Quadratic", "Cubic", "Quartic"]
print("What type of equation do you want to solve?")
print("1. Quadratic equation")
print("2. Cubic equation")
print("3. Quartic equation")
choice = int(input("Enter your choice: "))
print(f"you have chosen {eqn[choice-1]} equation")