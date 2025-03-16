print('This is a code designed to calculate compound interest')
print('Please enter the following details')
p = float(input('Enter the principal amount: '))
r = float(input('Enter the rate of interest: '))
t = float(input('Enter the time period in years: '))
n = float(input('Enter the number of times interest is compounded per year: '))
a = p*(1+(r/n))**(n*t)
ci = a-p
print('The amount is: $', a)
print('The compound interest is: $', ci)
# The compound interest is calculated using the formula: A = P(1 + r/n)^(nt) - P