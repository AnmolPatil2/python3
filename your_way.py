t = int(input(""))
for e in range(t):
    o = []
    n = int(input(""))
    l = list(input(""))
    for s in l:
        if(s == "S"):

            o.append("E")
        else:
            o.append("S")
    o = "".join(x for x in o)
    print("Case #"+str(e+1)+": " + o)
