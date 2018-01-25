# # Problem 1. Passed
# grade  = float(input())
# if grade >= 3:
#     print('Passed!')

# # Problem 2. Passed or Failed
# grade = float(input())
# if grade >= 3:
#     print('Passed!')
# else:
#     print('Failed!')

# # # Problem 3. Back in 30 Minutes
# hours, minutes = int(input()), int(input())
# minutes += 30
# minutes, hours = (minutes - 60, hours + 1) if minutes > 59 else (minutes, hours)
# hours = 0 if hours > 23 else hours
# print('{0}:{1:02d}'.format(hours, minutes))

# # Problem 4. Month Printer
# n = int(input())
# months_choices = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
#                   'September', 'October', 'November', 'December']
# print(months_choices[n - 1]) if (1 <= n <= 12) else print('Error!')

# # Problem 5. Foreign Languages
# country = input()
# if country == 'USA' or country == 'England':
#     print('English')
# elif country == 'Spain' or country == 'Argentina' or country == 'Mexico':
#     print('Spanish')
# else:
#     print('unknown')

# # 7. Problem 6. Theatre Promotions
# day_of_week = input()
# age = int(input())
# if 0 <= age <= 122:
#     if day_of_week == 'Weekday':
#         if 0 <= age <= 18 or 64 < age <=122:
#             print('12$')
#         elif 18 < age <= 64:
#             print('18$')
#     elif day_of_week == 'Weekend':
#         if 0 <= age <= 18 or 64 < age <=122:
#             print('15$')
#         elif 18 < age <= 64:
#             print('20$')
#     elif day_of_week == 'Holiday':
#         if 0 <= age <= 18:
#             print('5$')
#         elif 18 < age <= 64:
#             print('12$')
#         elif 64 < age <= 122:
#             print('10$')
# else:
#     print('Error!')

# # 8. Problem 7. Divisible by 3
# def divisible_by_three():
#     for i in range(1, 101):
#         if i % 3 == 0:
#             yield i
# for i in divisible_by_three():
#     print(i)

# # 9. Problem 8. Sum of Odd Numbers
# total = 0
# def sum_of_odd_numbers(num, inp):
#     if inp == 0:
#         return
#     global total
#     total += num
#     print(num)
#     sum_of_odd_numbers(num + 2, inp - 1)
#     return total
#
# def represent():
#     n = int(input())
#     sequence = 1
#     result = sum_of_odd_numbers(sequence, n)
#     print('Sum: {}'.format(result))
# represent()

# # 10. Problem 9. Multiplication Table
# n = int(input())
# for i in range(1, 11):
#     print('{} X {} = {}'.format(n, i, n * i))

# # 11. Problem 10. Multiplication Table 2.0
# multiplyer = int(input())
# start = int(input())
# if start > 10:
#     print('{} X {} = {}'.format(multiplyer, start, multiplyer * start))
# else:
#     for i in range(start, 11):
#         print('{} X {} = {}'.format(multiplyer, i, multiplyer * i))

# # 12. Problem 11. Odd Number
# n = abs(int(input()))
# while n % 2 == 0:
#     print('Please write an odd number.')
#     n = abs(int(input()))
# print('The number is: {}'.format(n))

# 13. Problem 12. Number checker
n = input()
try:
    int(n)
    print('It is a number.')
except:
    print('Invalid input!')
