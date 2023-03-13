# write a program to check if the input year is leap year or not

year = int(input("Enter any year : "))

if year % 400 == 0 and year % 100 == 0:
    print("Given year is Leap year")
else:
    print("Given year is not Leap year")
