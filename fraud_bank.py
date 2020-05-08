
n, d = [int(x) for x in input("").split()]
l = [int(x) for x in input("").split()]

if(d % 2 == 0):

    e = int(d/2)-1
    d1 = e+1

else:
    e = int(d//2)
    d1 = 0
z = 0


def mo(l, k, z):

    l.sort()

    if(d1 == 0):

        if(l[e] * 2 <= k):
            z = z+1

    else:

        if((l[e]+l[d1]) < k):

            z = z + 1
    return z


for x in range(d, n):

    z = mo(l[x-d:x], l[x], z)

print(z)
