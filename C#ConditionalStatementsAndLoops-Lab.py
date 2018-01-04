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