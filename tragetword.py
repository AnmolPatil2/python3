l = input("").split(" ")
target = list(input(""))
di = {}
ccc = 0
for i in range(len(l)):
    di[i] = list(l[i])
print(di)
r = [0]*len(l)
f = {}
print(r)
for j in target:
    f[j] = []
for j in range(len(target)):
    for i in range(len(l)):
        if target[j] in di.get(i):
            print(j)
            r[i] += 1
            f[target[j]].append(i)
print(r, f)
m = r[0]
for i in range(len(r)):
    if(r[i] >= m):
        m = r[i]
        mi = i
fml = []
for i, k in f.items():
    for x in k:
        if(x == mi):
            fml.append(i)
            ccc += 1
for x in fml:

    del f[x]
print(f)
