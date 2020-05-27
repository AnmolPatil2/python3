class point:
    def __init__(self, x):
        self.x = x

    def cor(self):
        return self.x


class rectange:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

    def area(self):
        return self.x*self.y

    def reshape(self):
        self.x = self.c.cor()
        self.y = self.c.cor()+self.x
        return self.x, self.y


l = point(4)
rect = rectange(2, 3, l)
print(rect.area())
print(rect.reshape())
