
from itertools import combinations
arr = []


def rSubset(arr, r):

    return list(combinations(arr, r))


# Driver Function
a = int(305201920/100000)
for i in range(1, a):
    arr.append(i)
print(arr)
for r in range(3, 15):
    if(sum((rSubset(arr, r))) == 305201920):
        print((rSubset(arr, r)))
