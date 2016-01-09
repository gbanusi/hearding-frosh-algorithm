__author__ = 'gbbanusic'


class Triangle:
    EPSILON = 0.005

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def signed_triangle_area(self):
        return self.a.x * self.b.y - self.a.y * self.b.x + self.a.y * self.c.x - self.a.x * self.c.y + self.b.x * self.c.y - self.c.x * self.b.y


    def ccw(self):
        return self.signed_triangle_area() > self.EPSILON
