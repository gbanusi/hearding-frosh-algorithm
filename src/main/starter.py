from src.main.components.Point import Point
from src.main.components.HerdingFrosh import HerdingFrosh

__author__ = 'gbbanusic'

# list = [Point(-6.7, 29.77), Point(-10.25, 36.46), Point(-11.43, 36.86), Point(-28.68, 35.65),
#         Point(-45.86, 28.95), Point(-47.78, 21.35), Point(-50.11, -24.34), Point(-41.46, -42.94),
#         Point(1.51, -47.88), Point(32.13, -48.82), Point(44, -30.47), Point(45.45, 19.69), Point(42.77, 34.68),
#         Point(26.6, 48.12), Point(1.48, 23.4)]

# num_of_test_case = input()
# while num_of_test_case > 0:
#     num_of_frosh = input()
#     for i in range(0, num_of_frosh):
#         list.append(Point(input("%d %d")))
#     num_of_test_case -= 1

# with open("../example.txt") as f:
#     num_of_test_case = [int(x) for x in f.readline().split()][0]
#     f.readline()
#     num_of_points = []
#     nums = []
#     for j in range(0, num_of_test_case):
#         num_of_points.append([int(x) for x in f.readline().split()][0])
#         for i in range(0, num_of_points[j]):
#             line = f.readline()
#             nums.extend([float(x) for x in line.split()])
#         blank = f.readline()
#
# case = []
# last = 0
# for rang in num_of_points:
#     list = []
#     for i in range(last, rang*2-1 + last, 2):
#         list.append(Point(nums[i], nums[i+1]))
#     case.append(list)
#     last += rang*2
#
# for i in range(0, len(case)):
#     polygon = HerdingFrosh(case[i])
#     print polygon.calculate_perimeter()

print HerdingFrosh(
    [Point(1, 1), Point(-1, 1), Point(1, -1), Point(-1, -1), Point(0.3, 0), Point(-0.4, 0.7), Point(0, -0.99),
    Point(-0.9, 0.7), Point(-0.1, 0.9), Point(-0.0, -0.9)]).calculate_perimeter()
