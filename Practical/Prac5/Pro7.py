# write a python program takes in number and find the sum of digits in a number
number = int(input("Enter any number : "))
sum = 0
while number > 0:
    rem = number % 10
    sum = sum + rem
    number = number // 10
print(sum)