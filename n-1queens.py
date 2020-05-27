k = int(input(""))
r = [x for x in range(k)]

p = 0
tc = 0
while(p != k and tc < k-1):
    t = []
    x = 0
    ff = 0
    tc = 0

    for i in range(k):
        f = 0
        for j in r:

            x = 0
            c = 0
            while(x < len(t)):
                if(abs(t[x]-i)-abs(t[x+1]-j) != 0):
                    c += 2
                x += 2

            if(c == len(t)):
                f = 1
                for x in range(k):
                    if(x == j):
                        print("*", end="")
                    else:
                        print(".", end="")
                print()
                r.remove(j)
                t.append(i)
                t.append(j)
                tc += 1

                break
        if(f == 0):
            if(ff == 0):
                ff = 1
                for x in range(k):
                    print(".", end="")
                print()
            else:

                break
