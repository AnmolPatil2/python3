
n = int(input(""))
a = [[int(x) for x in (input("").split())] for _ in range(n)]
l = []
t = int(input(""))
for _ in range(t):

    tp, e, b, c = [int(x) for x in (input("").split())]
    e -= 1
    b -= 1
    c -= 1

    if(tp == 1):

        if(b == n-1):
            for x in range(0, e):
                for y in range(0, n):
                    a[x][y] = a[x][y]
            for x in range(e, b+1):
                for y in range(0, n):
                    a[x][y] = a[x][y] ^ c
        else:
            for x in range(0, e):
                for y in range(0, n):
                    a[x][y] = a[x][y]
            for x in range(e, b+1):
                for y in range(0, n):
                    a[x][y] = a[x][y] ^ c
            for x in range(b+1, n):
                for y in range(0, n):
                    a[x][y] = a[x][y]


print(a)
