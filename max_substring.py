n = int(input(""))
for _ in range(n):
    m = int(input(""))
    l = list(input(""))
    di = {}
    for i in l:
        di[i] = l.count(i)
    x = list(di.values())
    print(x)
    m = max(x)
    a = len(l)-m
    print(m, a)
    if(m > a):
        m = a+1
    print(m+a)
