
from itertools import permutations_with_replacement
arr = []
c = 0
n, m, i = [int(x) for x in (input("").split())]
l = [int(x) for x in (input("").split())]
for x in (list(permutations_with_replacement(l, n))):
    if(sum(x) % m == 0):
        c += n
        print(x)
print(c)
