a = input("Enter the number : ")
print(f"Multiplication table of {a} is \n")

try:
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a)*i}")
except Exception as e:
    print("invalid input")

print("Some lines of code")
print("End of Program")
