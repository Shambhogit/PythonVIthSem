dic = {
    "Harry": "Human being",
    "Spoon": "Object"
}

emp_number = {
    12: "shambho",
    13: "Kisan",
    14: "Karan",
    15: "Vishal"
}

# print(emp_number[12])  # this line will throw error if key is not present in dictionari
# print(emp_number.get(15))  # this line will not throw error if key is not present in dictionary
print(emp_number.keys())
print(emp_number.values())
print(emp_number.items())