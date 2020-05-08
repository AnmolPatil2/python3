t = int(input(""))


def pal(l):

    co = {}
    nos = []
    f = 0
    for x in l:
        y = l.count(x)
        if(x not in nos):
            nos.append(x)

            if(y % 2 == 0):
                continue
            else:
                if(f == 0):
                    f = 1
                else:
                    return 0

    return 1


for ca in range(t):
    n, p = [int(x) for x in (input("").split())]
    li = list(input(""))
    to = 0
    for i in range(p):

        l, r = [int(x) for x in (input("").split())]

        to += pal(li[l-1: r])
    ca += 1
    print("Case #"+str(ca)+": " + str(to))
