# Write a python function that accepts a string and calculate the number of upper case latters and lower case letters

line = list(input("Enter the input String: "))
upper_case_count = 0
lower_case_count = 0

for char in line:
    if char.isupper():
        upper_case_count = upper_case_count + 1
    elif char.islower():
        lower_case_count = lower_case_count + 1

print("Count of upper case characters in line is : ", upper_case_count)
print("Count of lower case characters in line is : ", lower_case_count)
