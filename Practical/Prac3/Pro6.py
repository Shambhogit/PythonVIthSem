# Write a program to calculate volume and surface area of a cylinder
# volume of cylinder is pi*r*r*h
# surface area is 2*pi*r*h + 2*pi*r*r

pi = 3.14
height = int(input("Enter the height of cylinder : "))
radius = int(input("Enter the Radius of cylinder : "))

volume = pi * radius * radius * height
surface_area = (2 * pi * radius * height) + (2 * pi * radius * radius)

print("Volume of cylinder is : ", volume)
print("Surface Area of cylinder is : ", surface_area)
