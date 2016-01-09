from src.main.components.Point import Point
from src.main.components.Triangle import Triangle

__author__ = 'gbbanusic'
import math


def distance(a, b):
    return math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y))


def calculate_length(list):
    sum = 0
    for i in range(0, len(list) - 1):
        sum += distance(list[i], list[i + 1])
    return sum


def collinear(p0, p1, p2):
    triangle = Triangle(p0, p1, p2)
    return triangle.signed_triangle_area() == 0


def leftlower(a, b):
    if a.x < b.x:
        return -1
    if a.x > b.x:
        return 1
    if a.y < b.y:
        return -1
    if a.y >= b.y:
        return 1


def clockwiseOrder(a, b):
    if a.x >= 0 and b.x < 0:
        return 1
    if a.x < 0 and b.x >= 0:
        return -1
    if a.x == 0 and b.x == 0:
        if a.y >= 0 or b.y >= 0:
            return a.y > b.y
        return b.y > a.y


    # compute the cross product of vectors (center -> a) x (center -> b)
    det = (a.x - 0) * (b.y - 0) - (b.x - 0) * (a.y - 0)
    if det < 0:
        return 1
    if det > 0:
        return -1

    # points a and b are on the same line from the center
    # check which point is closer to the center
    d1 = (a.x - 0) * (a.x - 0) + (a.y - 0) * (a.y - 0)
    d2 = (b.x - 0) * (b.x - 0) + (b.y - 0) * (b.y - 0)
    return d1 > d2


def findMinConvexHulls(hull1):
    from src.main.components.HerdingFrosh import HerdingFrosh
    best = -1;
    hull2 = []
    hull2.append(hull1[0])
    if Point(0, 0) in hull1:
        hull1.remove(Point(0, 0))
    hull1.remove(hull1[0])
    if len(hull1) == 1:
        return distance(Point(0, 0), hull1[0]) + distance(Point(0, 0), hull2[0])

    startPoint = hull2[0]
    endPoint = hull1[len(hull1) - 1]

    for elem in list(hull1):
        sum1 = -1
        sum2 = -1
        if len(hull1) == 1:
            sum1 = distance(Point(0, 0), hull1[0])
        else:
            sum1 = HerdingFrosh(list(hull1)).calculate_perimeter()
            sum1 -= distance(Point(0, 0), endPoint)

        if len(hull2) == 1:
            sum2 = distance(Point(0, 0), hull2[0])
        else:
            sum2 = HerdingFrosh(list(hull2)).calculate_perimeter()
            sum2 -= distance(Point(0, 0), startPoint)

        sum = sum1 + sum2

        if best == -1 or best > sum:
            best = sum
        hull1.remove(elem)
        hull2.append(elem)

    return best
