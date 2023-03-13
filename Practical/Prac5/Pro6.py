# write a python program to revers number

number = int(input("Enter any number : "))
rev_number = 0

while number > 0:
    rem = number % 10
    rev_number = (rev_number * 10) + rem
    number = number // 10

print(rev_number)