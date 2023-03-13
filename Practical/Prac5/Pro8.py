# write a python program that taes a number and check whether it is palindrome or not

number = int(input("Enter any number : "))

num = number
rev_number = 0

while number > 0:
    rem = number % 10
    rev_number = (rev_number * 10) + rem
    number = number // 10

if rev_number == num:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")