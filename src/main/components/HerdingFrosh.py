from src.main.components.EuclideanGeom import *
from src.main.components.Point import Point
from src.main.components.Triangle import Triangle

__author__ = 'gbbanusic'


class HerdingFrosh:
    def __init__(self, points):
        # number of given herding frosh points
        self.n = len(points)
        # minimal convex polygon
        self.convexPoint = []
        # given points
        self.points = points
        self.points.append(Point(0, 0))
        # first point in convex hull
        self.top = -1

        # generate convex hull
        self.generate_convex_hull()

    def generate_convex_hull(self):
        if self.n <= 3:
            i = 0
            # Creating convex hull with 3 points.
            for point in self.points:
                self.convexPoint.append(point)
                i += 1
            return

        # Removing duplicates and sorting by leftlower.
        self.sort_and_remove_duplicates()

        self.first_point = self.points[0]
        self.points.pop(0)
        # Sort by angel
        self.points = sorted(self.points, cmp=self.smaller_angle)

        # add the lowest left
        self.add_point(self.first_point)
        # add the next to the lowest left sorted by angel
        self.add_point(self.points[0])
        self.points.append(self.first_point)
        i = 1

        while i < self.n:
            triangle = Triangle(self.convexPoint[self.top - 1], self.convexPoint[self.top], self.points[i])
            if triangle.ccw() is False:
                self.remove_point(self.convexPoint[self.top])
            else:
                self.add_point(self.points[i])
                i += 1

    def sort_and_remove_duplicates(self):
        if len(self.points) <= 1:
            return
        self.points = sorted(self.points, cmp=leftlower)
        oldn = self.n
        hole = 1
        for i in range(1, oldn - 1):
            if self.points[hole - 1] == self.points[i] and self.points[hole - 1] == self.points[i]:
                self.n -= 1
            else:
                self.points[hole] = self.points[i]
                hole += 1
        self.points[hole] = self.points[oldn - 1]

    def add_point(self, point):
        self.top += 1
        self.convexPoint.append(point)

    def remove_point(self, point):
        self.top -= 1
        self.convexPoint.remove(point)

    def smaller_angle(self, a, b):

        if collinear(self.first_point, a, b):
            if distance(self.first_point, a) <= distance(self.first_point, b):
                return -1
            else:
                return 1

        triangle = Triangle(self.first_point, a, b)
        if triangle.ccw():
            return -1
        else:
            return 1

    def calculate_perimeter(self):
        suma = 0
        for i in range(0, len(self.convexPoint) - 1):
            suma += distance(self.convexPoint[i], self.convexPoint[i + 1])
        suma += distance(self.convexPoint[0], self.convexPoint[len(self.convexPoint) - 1])
        sol = self.connect_to_origin()
        # dodaj najmanji put do ishodista i oduzmi duzinu koja spaja
        # tocke u convexnom ljusci + 2 za spajanje sa ishodistem
        suma = suma + sol[0] - sol[1] + 2
        return suma

    def connect_to_origin(self):
        if Point(0, 0) in self.convexPoint:
            return [0, 0]
        self.points = sorted(self.points, cmp=clockwiseOrder)
        self.points.remove(Point(0, 0))
        min = -1
        bet = -1
        for i in range(0, len(self.convexPoint)-1):

            lista = []
            between = distance(self.convexPoint[i], self.convexPoint[(i + 1)])
            ft = self.points.index(self.convexPoint[i])
            nd = self.points.index(self.convexPoint[(i + 1)]) + 1
            while ft != nd:
                lista.append(self.points[ft])
                ft += 1
                if ft == nd:
                    break
                ft %= len(self.points)

            bestHullsLength = findMinConvexHulls(lista)
            # najmanji opseg svih permutacija konveksnih ljuski, bez spajanja
            temp = bestHullsLength
            if min == -1 or temp < min:
                min = temp
                bet = between

        lista = []
        between = distance(self.convexPoint[0], self.convexPoint[len(self.convexPoint)-1])
        ft = self.points.index(self.convexPoint[len(self.convexPoint)-1])
        nd = self.points.index(self.convexPoint[0]) + 1
        while ft != nd:
            lista.append(self.points[ft])
            ft += 1
            if ft == nd:
                break
            ft %= len(self.points)
        bestHullsLength = findMinConvexHulls(lista)
        # najmanji opseg svih permutacija konveksnih ljuski, bez spajanja
        temp = bestHullsLength
        if min == -1 or temp < min:
           min = temp
           bet = between

        return [min, bet]



