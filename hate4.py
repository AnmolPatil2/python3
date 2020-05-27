t = int(input(""))
for i in range(t):
    b = []
    l = list(input(""))
    print(l)
    for j in range(len(l)):
        if(l[j] == "4"):
            l[j] = "3"
            b.append("1")
        else:
            b.append("0")
    b = ''.join(x for x in b)
    a = ''.join(x for x in l)
    i += 1
    print("Case #"+str(i)+": " + a + " "+b)
