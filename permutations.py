from itertools import permutations

# Get all permutations of [1, 2, 3]
l = []
for i in range(0, 100):
    l.append(i)
perm = permutations(l)

# Print the obtained permutations
for i in (perm):
    print(i)
