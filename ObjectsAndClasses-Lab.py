# 1. Lab: Objects and Classes
# I. Using the Built-in .NET Classes

# # 2. Day of Week
# from datetime import datetime
#
# days = ['Monday', 'Tuesday', 'Wedensday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# d = datetime.strptime('18-04-2016', '%d-%m-%Y')
#
# print(days[d.weekday()])

# # 3. Randomize Words
# import random
# n = input().split(' ')
# random.shuffle(n)
# print(n)

# # II. Defining Simple Classes
# # 5. Distance Between Points
# from math import sqrt
# class Point():
#     def __init__(self):
#         self.x1_y1 = input().split(' ')
#         self.x2_y2 = input().split(' ')
#
#         self.x1_y1 = [int(x) for x in self.x1_y1]
#         self.x2_y2 = [int(x) for x in self.x2_y2]
#         # self.calc_distance(self.x1_y1, self.x2_y2) # Version 1
#
#     # def calc_distance(self, p1, p2): # Version 1
#     #     side_a = p1[0] - p2[0]
#     #     side_b = p1[1] - p2[1]
#
#     def calc_distance(self):
#         side_a = self.x1_y1[0] - self.x2_y2[0]
#         side_b = self.x1_y1[1] - self.x2_y2[1]
#
#         result = side_a**2 + side_b**2
#         # print('{0:.3f}'.format(sqrt(result))) # Version 1
#         return sqrt(result)
#
# # Point() # Version 1
# a = Point().calc_distance()
# print('{0:.3f}'.format(a))

# # 6. Closest Two Points
# from math import sqrt
# from itertools import combinations
# class Point():
#     def __init__(self):
#         self.n = int(input())
#         self.array = []
#
#         for i in range(self.n):
#             self.s = input().split(' ')
#             self.s = [int(x) for x in self.s]
#             self.array.append(self.s)
#
#     def find_closest_points(self):
#         closest = []
#         best_num = None
#         prod = combinations(self.array, 2)
#         for i in prod:
#             dist = sqrt((i[1][0] - i[0][0]) ** 2 + (i[1][1] - i[0][1]) ** 2)
#             if best_num == None:
#                 best_num = dist
#                 closest.append(i)
#             else:
#                 if dist < best_num:
#                     best_num = dist
#                     closest = []
#                     closest.append(i)
#         print('{0:.3f}'.format(best_num))
#         for k in closest:
#             print('({}, {})'.format(k[0][0], k[0][1]))
#             print('({}, {})'.format(k[1][0], k[1][1]))
#
#
# Point().find_closest_points()

# # 7. Rectangle Position
# class Rectangle():
#     first_rectangle = input().split(' ')
#     second_rectangle = input().split(' ')
#
#     first_rectangle = [int(x) for x in first_rectangle]
#     second_rectangle = [int(x) for x in second_rectangle]
#
#     f_left, f_top, f_width, f_height = first_rectangle[0], first_rectangle[1], first_rectangle[2], first_rectangle[3]
#     s_left, s_top, s_width, s_height = second_rectangle[0], second_rectangle[1], second_rectangle[2], second_rectangle[3]
#
#     f_bottom, f_right = f_top + f_width, f_left + f_height
#     s_bottom, s_right = s_top + s_width, s_left + s_height
#
#     def is_inside(self):
#         if self.f_left >= self.s_left and self.f_right <= self.s_right and self.f_top <= self.s_top and \
#             self.f_bottom <= self.s_bottom:
#             print('Inside')
#         else:
#             print('Not inside')
#
# Rectangle().is_inside()

# 8. Sales Report
class Sale():
    n = int(input())

    def read_sale(self):
        d = {}
        for i in range(self.n):
            l = input().split(' ')
            if l[0] in d:
                d[l[0]] += float(l[2]) * float(l[3])
            else:
                d[l[0]] = float(l[2]) * float(l[3])

        for key, value in sorted(d.items()):
            print('{} -> {:.2f}'.format(key, value))

Sale().read_sale()
