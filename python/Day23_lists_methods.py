l = [1, 1, 1, 3, 5, 66, 2]
print(l)

l.append(44)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

print(l.index(5))

print(l.count(1))

m = l.copy()
m[3] = 44
print(l)

l.insert(1, 899)
print(l)

n = [200, 300, 400]
l.extend(n)
print(l)
