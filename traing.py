t = int(input(""))
for ca in range(t):

    n, p = [int(x) for x in (input("").split())]
    l = [int(x) for x in (input("").split())]
    arr = [0 for x in range(p+3)]
    j = 0
    s = 0
    f = []
    for x in range(p-1, n):
        for i in range(p):
            arr[j] = l[x]-l[j]

            s += arr[j]
            j += 1
        j = j-p
        f.append(s)
    to = min(f)
    if(to < 0):
        to = 0
    ca += 1
    print("Case #"+str(ca)+": " + str(to))
