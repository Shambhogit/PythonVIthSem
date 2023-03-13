# write a python program to print fibonacci series

number = int(input("Enter length of series : "))

num1 = 0
num2 = 1
num3 = 0
print(num1, num2, end=" ")
for i in range(number-2):
    num3 = num1 + num2
    print(num3, end=" ")
    num1 = num2
    num2 = num3

