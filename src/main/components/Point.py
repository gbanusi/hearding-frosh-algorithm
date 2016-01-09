__author__ = 'gbbanusic'


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + \
               str(self.y) + ")"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def getX(self):
        return self.x

    def getY(self):
        return self.y
