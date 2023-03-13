# there are four types of arguments that we can provide in a function
# 1.Default Arguments
# 2.Keyword arguments
# 3.Variable length arguments
# 4.Required arguments

# Default Arguments
# def average(a=12, b=16):
#     print("The average is :", (a + b) / 2)


# average() #it will take default arguments 12,16
# average(4) #it will take a=4 and b=16(default)
# average(10, 8) #it will replace the default arguments

# keyword arguments
# average(a=10, b=33)
# average(b=11, a=55)

#variable length arguments

def average(*numbers): #numbers type is tuple
    sum1 = 0
    for i in numbers:
        sum1 = sum1 + i
    # print("Average is : ", sum / len(numbers))
    return sum1 / len(numbers)

# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
