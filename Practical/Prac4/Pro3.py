# write a progarm to check the largest number among the three numbers

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

if a > b and a > c:
    print("largest number is", a)
elif b > a and b > c:
    print("largest number is", b)
else:
    print("largest number is", c)
