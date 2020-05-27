n = int(input(""))
l = [int(x) for x in (input("").split())]
d = []

z = 0
g = [0]
f = [0 for i in range(len(l))]

p = 0
for x in range(0, n):
    if(len(d) == 0):
        d.append(l[x])

        
    elif(l[x] == -d[-1]):
        d.pop()

        f[p] += 2

        

    else:
        d.append(l[x])

        p += 1

print(max(f))
