t = int(input(""))
for _ in range(t):
    l = []
    c = 0
    n = int(input(""))
    for i in range(n):
        x = [int(x) for x in (input("").split(" "))]

        l.append(x)
    m = len(x)
    for i in range(n):
        for j in range(m):
            for x in range(n):
                for y in range(m):

                    if(l[i][j] > l[x][y] and x >= i and y >= j):
                        c += 1
    print(c)
