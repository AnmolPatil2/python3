import numpy as np
n = int(input(""))
a = [[int(x) for x in (input("").split())] for _ in range(n)]
l = []
t = int(input(""))
for _ in range(t):

    tp, e, b, c = [int(x) for x in (input("").split())]
    e -= 1
    b -= 1

    if(tp == 1):
        for x in range(0, e):
            l.append(a[x])
        arr = np.array(a[e:b+1])

        for x in arr:
            x = np.bitwise_xor(x, c)

            l.append(x.tolist())

        if(n != b+2):
            for x in range(b+1, n):
                l.append(a[x])
    a = l


s = 0
for x in range(0, n-1):
    s += a[x][x]
print(s)
