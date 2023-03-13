""" write a python program to perform following
 operation on set intersection of sets union of
 sets difference symmetric difference clear set """

A = {4, 5, 6, 7, 8, 9, 3, 2}
B = {66, 5, 2, 6, 7, 99, 9}

print(A.intersection(B))  # it prints elements in both set
print(A.union(B))  # it prints both the set, and avoid repetation
print(A.difference(B))  # it prints different values of A wrt B
print(A.symmetric_difference(B))  # it prints different elements of both set
A.clear()  # it clears all the elements in set
