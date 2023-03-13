# write a python program to find common items from two lists
a = int(input("Enter size of list 1 : "))
b = int(input("Enter size of list 2 : "))

print("Enter element in list_one")
list_one = [int(input()) for i in range(a)]

print("Enter element in list_one")
list_two = [int(input()) for j in range(b)]

list_common = []
for i in range(len(list_one)):
    for j in range(len(list_two)):
        if list_one[i] == list_two[j]:
            list_common.append(list_one[i])

print("common elements in list_one", list_one, "and list_tow", list_two)
print(list_common)

