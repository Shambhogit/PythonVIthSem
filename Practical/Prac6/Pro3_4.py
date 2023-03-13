# write a python program to get the largest number from a list
# write a python program to get the smallest number from a list
numbers = [22, 54, 1, 66, 75, 87, 33, 200, 56, 34]
large_number = 0

for a in numbers:
    if large_number < a:
        large_number = a

small_number = large_number
for a in numbers:
    if a < small_number:
        small_number = a

print("small number from list is : ", small_number)
print("large number from list is : ", large_number)
