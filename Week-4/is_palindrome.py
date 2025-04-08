print("This is a program to check whether a string\n"
"reads the same way backwards\n"
"kindly folllow the instructions:  \n\n")
def is_palindrome(strings):
    strings = strings.lower()
    if strings == strings[::-1]:
        print(True)
    else:
        print(False)
    return
is_palindrome(str(input("Kindly enter a string: ")))