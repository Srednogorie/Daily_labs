# 1. Exercises: Objects and Classes
# 2. Count Working Days
# 2. Day of Week
import datetime
start = input()
end = input()

# days = ['Monday', 'Tuesday', 'Wedensday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'Octomber', 'November', 'December']
holydays = ['1 January', '3 March', '1 May', '6 May', '24 May', '6 September', '22 September', '1 November',
            '24 December', '25 December', '26 December']
start_d = datetime.datetime.strptime(start, '%d-%m-%Y')
end_d = datetime.datetime.strptime(end, '%d-%m-%Y')

r = abs((start_d - end_d).days) + 1

count = 0

date_list = [start_d + datetime.timedelta(days=x) for x in range(r)]
date_list = [x.strftime('%d %B') for x in date_list]

for i in date_list:
    check_date = datetime.datetime.strptime(i, '%d %B')
    if i in holydays or check_date.weekday() in range(6, 8):
        pass
    else:
        count += 1

print(count)