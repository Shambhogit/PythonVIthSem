# write a python function calculate the factorial of number

def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num-1)


print(factorial(5))