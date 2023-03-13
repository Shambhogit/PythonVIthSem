# Create a tuple and find the minimum and maximum number from it

size = int(input("Enter the size of tuple : "))
tup_1 = tuple(int(input()) for a in range(size))
print(tup_1)

maximum = 0
for a in tup_1:
    if a > maximum:
        maximum = a

minimum = maximum
for a in tup_1:
    if a < minimum:
        minimum = a

print("Minimum number from tuple is :", minimum)
print("Maximum number from tuple is :", maximum)

