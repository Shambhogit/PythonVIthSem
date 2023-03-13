# write a python program to select the even items of a list

marks = [22, 44, 53, 12, 66, 45]

print(marks)
print("Following are even numbers from list")
for i in marks:
    if i % 2 == 0:
        print(i, end=" ")
