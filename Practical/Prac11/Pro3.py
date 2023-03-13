"""
Write a python function that accepts a string and
calculate the number of upper case letters and lower
case letters
"""
def cal_upper_lower(string_line):
    count_upper = 0
    count_lower = 0

    for char in string_line:
        if char.isupper():
            count_upper = count_upper + 1
        elif char.islower():
            count_lower = count_lower + 1
    print("Upper Count :", count_upper)
    print("Lower Count :", count_lower)

cal_upper_lower("Shambho Ramchandra Jaybhaye")
