print('This is a code designed to calculate simple interest')
print('Please enter the following details')
p = float(input('Enter the principal amount: '))
r = float(input('Enter the rate of interest: '))
t = float(input('Enter the time period in years: '))
a = p*(1+(r/100)*t)
si = a-p
print('The amount is: $', a)
print('The simple interest is: $', si)
# The simple interest is calculated using the formula: A = P(1 + rt) - P