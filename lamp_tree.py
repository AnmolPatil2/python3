n, q = [int(x) for x in input("").split()]
di = {}
l = []
for i in range(0, n):
    di[i+1] = []
    l.append(1)
for _ in range(n-1):
    a, b = [int(x) for x in input("").split()]
    di[a].append(b)
    di[b].append(a)
for _ in range(q):
    a, b = [int(x) for x in input("").split()]
    if(a == 1):
        l[b-1] = ~l[b-1]
    else:
        c = 0
        for x in di.get(b):
            if(l[x-1] == 1):
                c += 1
        print(c)
