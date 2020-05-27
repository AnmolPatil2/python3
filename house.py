t = int(input(""))
for z in range(t):
    n, b = [int(x) for x in (input("").split())]

    l = [int(x) for x in (input("").split())]
    l.sort()
    s = 0
    c = 0

    for i in l:
        s += i
        if(b < s):
            break
        else:
            c += 1

    z += 1
    print("Case #"+str(z)+": " + str(c))
