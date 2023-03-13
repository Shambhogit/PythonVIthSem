import numpy as np

print("Enter 1st list")
list_one = [[int(input()) for i in range(3)] for j in range(3)]

print("Enter 2nd list")
list_two = [[int(input()) for k in range(3)] for l in range(3)]

print(list_one)
print(list_two)

list_add = np.add(list_one, list_two)
list_sub = np.subtract(list_one, list_two)
list_mul = np.multiply(list_one, list_two)
list_div = np.divide(list_one, list_two)

print("Addition of list is ")
print(list_add)

print("Subtraction of list is ")
print(list_sub)

print("Multiplication of list is ")
print(list_mul)

print("division of list is ")
print(list_div)
