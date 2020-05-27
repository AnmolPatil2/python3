import itertools
n, m, ll = [int(x) for x in input("").split()]
tc = 0
l = [int(x) for x in input("").split()]
x = itertools.product(l, repeat=n)
for i in x:
    if(sum(i) % m == 0):
        tc += 1
print(tc)
