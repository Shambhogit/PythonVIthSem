# write a program to find out absolute value of an input number

number = int(input("Enter any number : "))
if number < 0:
    n = 1000000
    number = n + number
    absolute = n - number
    print(absolute)
else:
    print(number)