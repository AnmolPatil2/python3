import math


class dist:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def dis(self):
        return math.sqrt(abs(self.x-self.a)**2 + abs(self.y-self.b)**2)

    def mid(self):
        return (self.dis()/2)


x, y, a, b = [int(x) for x in input("").split()]
r = dist(x, y, a, b)
print("distance is {}".format(r.dis()))
print("mid point is {}".format(r.mid()))
