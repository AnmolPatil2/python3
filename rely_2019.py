import numpy as np
[n, m, c, r] = [int(x) for x in (input("").split())]
co = []
x = []
y = []
way = []


def caldis(x, y, a, b):

    if(x-a > 0):
        ax = -1
        w = "L"
    else:
        ax = 1
        w = "R"
    if(y-b > 0):
        ay = 1
        wn = "U"
    else:
        ay = -1
        wn = "D"
    cs = 0
    while(x != a or y != b):
        try:
            if(ma[x+ax][y] > ma[x][y+ay]):
                y += ay
                cs += ma[x][y+ay]
                way.append(wn)

            else:
                x += ax
                cs += ma[x+ax][y]
                way.append(wn)
        except:
            break
        print(cs)


for _ in range(c):
    x1, y1, co1 = ([int(x) for x in (input("").split())])
    x.append(x1)
    y.append(y1)
    co.append(co1)
xc = (sum(x))//c
yc = (sum(y))//c
if(xc-3 > 0 and yc-3 > 0):
    lx = np.linspace(xc-3, xc+2, 5)
    ly = np.linspace(yc-3, yc+2, 5)

l = []
for _ in range(m):
    s = input("").replace("#", "9")
    s = s.replace("~", "7")
    s = s.replace("*", "6")
    s = s.replace("+", "5")
    s = s.replace("X", "4")
    s = s.replace("H", "3")
    s = s.replace("_", "2")
    s = s.replace("T", "1")
    l.append(list(int(x) for x in s))
print(l)
ma = np.array(l)
print(ma)
