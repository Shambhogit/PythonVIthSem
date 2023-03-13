# to change in tuple
colors = ("Green", "Red", "Yellow", "White", "Black")
print(type(colors), colors)
temp = list(colors)
temp.append("Blue")
temp.pop(3)
temp[2] = "Oreange"
colors = tuple(temp)
print(type(colors), colors)
