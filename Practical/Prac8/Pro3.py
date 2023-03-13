# write a python program to find maximum and the minimum value in set
size = int(input("Enter size of set : "))
set_a = set(int(input()) for i in range(size))
print(set_a)
max_number = 0
for ma in set_a:
    if ma > max_number:
        max_number = ma

min_number = max_number
for m in set_a:
    if m < min_number:
        min_number = m

print("Maximum number in set is : ", max_number)
print("Minimum number in set is : ", min_number)