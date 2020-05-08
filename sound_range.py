t = int(input(""))
for _ in range(t):
    l, r, s = [int(x) for x in (input("").split())]
    mi = l//s if l % s == 0 else l//s+1

    ma = r//s
    if(mi == 0 or ma == 0 or mi > ma):
        mi = -1
        ma = -1
    print(str(mi)+" " + str(ma))
