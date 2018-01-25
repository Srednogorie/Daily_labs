# 1. More Exercises: Objects, Classes, Files and Exceptions
# I. Objects and Classes
# Problem 1. Order by Age
n = input().split(' ')
d = {}

while n[0] != 'End':
    d[n[0]] = {}
    d[n[0]]['id'] = n[1]
    d[n[0]]['age'] = n[2]
    n = input().split(' ')

d_sorted_list = sorted(d, key=lambda x: (d[x]['age']))
for i in d_sorted_list:
    print('{} with ID: {} is {} years old.'.format(i, d[i]['id'], d[i]['age']))