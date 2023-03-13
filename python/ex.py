import random
import string
s = 10
# line = input("Enter line to encrypt\n")
a = 'line = input("Enter line to encrypt\n")'

st = ''.join(random.choices(string.ascii_lowercase + string.digits, k=s))

print(str(st))