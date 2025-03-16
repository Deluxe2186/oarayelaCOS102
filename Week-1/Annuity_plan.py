print('This is a code designed to calculate Annuity plan')
print('Please enter the following details')
p = float(input('Enter the principal amount: '))
r = float(input('Enter the rate of interest: '))
t = float(input('Enter the time period in years: '))
n = float(input('Enter the number of times interest is compounded per year: '))
pmt = float(input('Enter the payment amount per period: '))
a = pmt*((1+r/n)**(n*t)-1)/(r/n)
print('The amount is: $', a)
# The annuity plan is calculated using the formula: A = PMT*((1+r/n)^(nt)-1)/(r/n)