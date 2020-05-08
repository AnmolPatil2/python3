t = int(input(""))
for _ in range(t):
    s = list(input(""))
    v = []
    c = []
    f = ""
    for i in s:
        if(i not in v):
            v.append(i)

            f += i+str(s.count(i))
    print(f)
