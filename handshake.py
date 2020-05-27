n = int(input(""))
di = {}
c = 0
for i in range(1, 4):
    l = [int(x) for x in input("").split()]
    a = l[0]
    l = l[1:]
    di[a] = l

for i, v in di.items():
    for j, val in di.items():
        if i in val:
            if j not in v:
                di[i].append(j)

for i, v in di.items():

    c += n-len(v)-1
    print(c)
a = (n-3)

c += int((a*(a-1))/2)

print(c)
