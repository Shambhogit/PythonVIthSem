# write the number in words for example 1234=> one two three four
number = tuple(input("enter number : "))

for num in number:
    if num == '0':
        print("zero", end=" ")
    elif num == '1':
        print("One", end=" ")
    elif num == '2':
        print("Two", end=" ")
    elif num == '3':
        print("Three", end=" ")
    elif num == '4':
        print("Four", end=" ")
    elif num == '5':
        print("Five", end=" ")
    elif num == '6':
        print("Six", end=" ")
    elif num == '7':
        print("Seven", end=" ")
    elif num == '8':
        print("Eight", end=" ")
    elif num == '9':
        print("Nine", end=" ")

