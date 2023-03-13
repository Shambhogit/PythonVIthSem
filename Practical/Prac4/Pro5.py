# Write a program to check if a number is positive negative of zero

number = int(input("Enter any number : "))

if number < 0:
    print("Number is Negative")
elif number == 0:
    print("Number is Zero")
else:
    print("Number is Positive")
