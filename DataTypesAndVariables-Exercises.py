# # 5. Variable in Hexadecimal Format
# hex = input()
# print(int(hex, 16))

# # 12. Convert Speed Units
# from decimal import Decimal, getcontext
# getcontext().prec = 7
# distance_meters, hours, minutes, seconds = Decimal(input()), Decimal(input()), Decimal(input()), Decimal(input())
# total_minutes = 0
# if hours > 0:
#     total_minutes += hours * 60
# total_minutes += minutes
# total_seconds = (total_minutes * 60) + seconds
#
# meters_per_second = distance_meters / total_seconds
# km_per_hour = (meters_per_second * 60 * 60) / 1000
# miles_per_hour = (meters_per_second * 60 * 60) / 1609
# print('{}'.format(meters_per_second))
# print('{}'.format(km_per_hour))
# print('{}'.format(miles_per_hour))

# # 13. Rectangle Properties
# import math
# width, height = float(input()), float(input())
# print('{0:g}'.format(2 * (width + height)))
# print('{0:g}'.format(width * height))
# print('{0:.13f}'.format(math.sqrt(width**2 + height**2)))

# # 15. Integer to Hex and Binary
# n = int(input())
# print(hex(n))
# print('{0:b}'.format(n))

# #17. * Comparing Floats
# a, b = float(input()), float(input())
# if abs(a - b) >= 0.000001:
#     print('False')
# else:
#     print('True')

# # 18. Print Part of the ASCII Table
# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# 20. * Thea the Photographer
# This problem is from the Programming Fundamentals Retake Exam (11 September 2016).
import math
n ,ft, ff, ut = int(input()), int(input()), int(input()), int(input())
useful_pics = math.ceil(n * (ff / 100))
filter_time = n * ft
upload_time = useful_pics * ut
total_seconds = filter_time + upload_time
numm = total_seconds
days, hours, minutes = 0, 0, 0
if numm//86400 >= 1:
    days = numm//86400
    numm -= days * 86400

if numm//3600 >= 1:
    hours = numm//3600
    numm -= hours * 3600

if numm//60 >= 1:
    minutes = numm//60
    numm -= minutes * 60

seconds = numm
print('{0:01d}:{1:02d}:{2:02d}:{3:02d}'.format(int(days), int(hours), int(minutes), int(seconds)))