# Program for match statment
x = int(input("Enter the value  of X : "))

match x :
    case 0:
        print("Value of x is 0")
    case 1:
        print("Value of x is one")
    case 2:
        print("Value of x is two")
    case 3:
        print("Value of x is three")
    case _:
        print("It is Default value")
