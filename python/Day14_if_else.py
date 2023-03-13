age = int(input("Enter your age : "))
print("Your age is ", age)

# Conditional operators
# >, <, >=, <=, ==, !=
'''
if a > 18:
    print("You can drive")
else:
    print("You cannot drive")
'''

if age < 0:
    print("Your age is not valid")
elif age > 17:
    print("You can drive vehicle")
else:
    print("You cannot drive vehicle")