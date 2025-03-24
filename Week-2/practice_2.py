# Input from user
m = float(input("Enter mass in kilograms: "))

# constant value for the speed of light in m/s
c = 299792458

#calculating energy using Einstein's equation
energy = m * c ** 2

# Displaying the result
print(f"The energy equivalent to {m} kg of mass is {energy} joules.")