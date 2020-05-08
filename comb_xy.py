from itertools import combinations


def iss(l):
    so = 0
    print(l)
    for x in l:
        so += x
    if so % k == 0:
        return l
    else:
        return 0


n, k = [int(x) for x in (input("").split())]
x = []
y = []
for _ in range(n):
    a, b = [int(x) for x in (input("").split())]
    x.append(a)
    y.append(b)
s = [x for x in combinations(y, k)]
for x in s:
    if(iss(x) != 0):
        print("ss")

print(s)
