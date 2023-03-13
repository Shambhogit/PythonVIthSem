# Write a python program to find the repeated items of a tuple
size = int(input("Enter size of tuple : "))
tup_1 = tuple(int(input()) for i in range(size))

print("Following are repeated items in tuple")
for i in range(len(tup_1)):
    for j in range(i+1, len(tup_1)):

        if tup_1[i] == tup_1[j]:
            print(tup_1[i])

