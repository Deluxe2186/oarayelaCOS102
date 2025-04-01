print("This is a program to determine the\n"
"Annual Tax Revenue (ATR) of various staff in a Fintech company\n"
"Based on their age and level of work experience")
print("Kindly enter the required information\n")

name = str(input("Enter name of staff: "))
age = int(input("Enter age of staff: "))
exp = int(input("Enter number of years of experience: "))
atr = ["N5,600,000", "N4,480,000", "N1,500,000", "N550,000"]

if exp > 25 and age >= 55:
    print("Name: ",name)
    print("Age: ",age)
    print("Years of experience: ",exp)
    print("ATR: ", atr[0])
elif exp > 20 and age >= 45:
    print("Name: ",name)
    print("Age: ",age)
    print("Years of experience: ",exp)
    print("ATR: ", atr[1])
elif exp > 10 and age >= 35:
    print("Name: ",name)
    print("Age: ",age)
    print("Years of experience: ",exp)
    print("ATR: ", atr[2])
elif exp <= 10 and age < 35:
    print("Name: ",name)
    print("Age: ",age)
    print("Years of experience: ",exp)
    print("ATR: ", atr[3])
