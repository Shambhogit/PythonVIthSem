# Write a program to convert bits to MB, GB, TB

bits = int(input("Enter the number of bits : "))
byt = bits/8
kb = byt/1024
mb = kb/1024
gb = mb/1024
tb = gb/1024

print(bits, " bits in KB is : ", kb)
print(bits, " bits in MB is : ", mb)
print(bits, " bits in GB is : ", gb)
print(bits, " bits in TB is : ", tb)

