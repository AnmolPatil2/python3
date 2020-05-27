import numpy as np


def skill(a, b):
    lc = 0
    if(a[0] == b[0]):
        lc = (int(a[1])+int(b[1]))
        print(lc)
    else:
        lc = 0
    a2 = set(a[2:-1])
    b2 = set(b[2:-1])
    lc += len(a2.intersection(b2))*len((a2.symmetric_difference(b2)))
    return lc


w, h = [int(x) for x in (input("").split(" "))]
l = []
for _ in range(h):

    s = input("")
    l.append(list((x) for x in s))
ma = np.array(l)

nd = int(input(""))
di = {}
for i in range(nd):
    l = [x for x in (input("").split(" "))]
    del l[2]
    di[i] = l

nd = int(input(""))
mg = {}
for i in range(nd):
    mg[i] = [x for x in (input("").split(" "))]
score = []
x = []
y = []
for val in di.keys():
    for val1 in di.keys():

        a = di.get(val)
        b = di.get(val1)

        score.append(skill(a, b))
        x.append(val)
        y.append(val1)

print(score)

i = 0
c = 0
x2 = {}
y2 = {}
f = []
c = w*h
while(i < h):
    j = 0
    while(j < w):
        if(ma[i][j] == "_"):
            q = score.index(max(score))
            f.append(y[q])
            f.append(x[q])
            x2[x[q]] = i

            y2[y[q]] = j
        j += 1
    i += 1
file = open('e2.txt', 'w')

for keys in di.keys():
    if(keys not in f):
        file.write("X"+"\n")
    else:
        file.write(str(x2[keys])+" " + str(y2[keys])+"\n")
while(i < h):
    j = 0
    while(j < w):
        if(ma[i][j] == "M"):
            c += 1
            file.write(str(i)+" " + str(j)+"\n")
        j += 1
    i += 1
z = (h*w)-c
for i in range(z):
    file.write("X"+"\n")
