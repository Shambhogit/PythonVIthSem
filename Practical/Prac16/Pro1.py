
def divide_numbers(a, b):
    try:
        div = a / b
        print(div)
    except ZeroDivisionError:
        print("Zero division error is occurred")


divide_numbers(12, 3)
divide_numbers(55, 3)
divide_numbers(14, 0)
divide_numbers(0, 14)


