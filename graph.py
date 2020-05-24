import random


class graph:

    con = {}
    cont = 0

    def node(self, x):
        self.con[x] = []

    def edge(self, x, y):
        self.con[x].append(y)
        self.con[y].append(x)


g = graph()
for i in range(6):
    g.node(i)
for j in range(10):
    a = (random.randrange(1, 6))
    b = (random.randrange(1, 6))
    g.edge(a, b)
for j in range(6):
    print(g.con[j])
