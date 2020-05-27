t = int(input(""))
n = []
v = []


def so(i, j):
    v[i], v[j] = v[j], v[i]
    n[i], n[j] = n[j], n[i]


for _ in range(t):
    n1, m = (input("").split())
    m = int(m)
    n.append(n1)
    v.append(m)
for i in range(0, t):
    for j in range(0, t-i-1):
        if(v[j] == v[j+1]):

            if(n[j] > n[j+1]):
                so(j, j+1)
        elif(v[j] < v[j+1]):
            so(j, j+1)
        else:
            continue

for i in range(0, t):
    print((n[i])+" " + str(v[i]))
