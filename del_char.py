n = int(input(""))
for _ in range(n):
    m = int(input(""))
    l = list(input(""))
    c = len(l)
    for i in range(1, len(l)):
        if(l[i] == l[i-1]):
            c -= 1
    print(c)
