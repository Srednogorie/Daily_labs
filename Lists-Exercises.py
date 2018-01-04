# # 2. Max Sequence of Equal Elements
# import re
#
# n = input()
# result = re.finditer(r'(\d)(?: \1)+', n)
#
# max_len, number = 0, ''
#
# for match in result:
#     if len(match.group(0)) > max_len:
#         max_len = len(match.group(0))
#         number = match.group(0)
# print(number)

# # 2. Max Sequence of Equal Elements - Version 1
# n = input()
# s = n.replace(' ', '')
#
# numm, count, final_numm, final_count = s[0], 1, '', 0
# for i in s[1:]:
#     if i == numm:
#         count += 1
#         if count > final_count:
#             final_count = count
#             final_numm = numm
#     else:
#         if count > final_count:
#             final_count = count
#             final_numm = numm
#         numm = i
#         count = 1
#
# print((final_numm + ' ') * final_count)

# # 3. Change List
# n = input()
# s = n.split(' ')
# que = True
#
# while que is True:
#     main_command = input()
#     if main_command != 'Even' and main_command != 'Odd':
#         commands = main_command.split(' ')
#         if commands[0] == 'Delete':
#             element = commands[1]
#             try:
#                 for i in s:
#                     if i == element:
#                         s = [x for x in s if x != i]
#                         break
#             except:
#                 pass
#         elif commands[0] == 'Insert':
#             element, position = commands[1], int(commands[2])
#             try:
#                 s.insert(position, element)
#             except:
#                 pass
#     else:
#         if main_command == 'Even':
#             for i in s:
#                 if int(i) % 2 == 0:
#                     print(i, end=' ')
#         elif main_command == 'Odd':
#             for i in s:
#                 if int(i) % 2 != 0:
#                     print(i, end=' ')
#         que = False

# # 4. Search for a Number
# n, comands = input().split(' '), input().split(' ')
# c_one, c_two, c_three = int(comands[0]), int(comands[1]), comands[2]
#
# result = n[c_two:c_one + 1]
#
#
# if c_three in result:
#     print('YES!')
# else:
#     print('NO!')

# # 6. * Array Manipulator
# n, que = input().split(' '), True
#
#
# def shift(array, index):
#     return array[index:] + array[:index]
#
#
# while que is True:
#     command = input().split(' ')
#     if command[0] == 'add':
#         n.insert(int(command[1]), command[2])
#     elif command[0] == 'addMany':
#         n[int(command[1]):int(command[1])] = command[2:]
#     elif command[0] == 'contains':
#         if command[1] in n:
#             print(n.index(command[1]))
#         else:
#             print('-1')
#     elif command[0] == 'remove':
#         del n[int(command[1])]   # del removes index where remove() first matchig value
#     elif command[0] == 'shift':
#         n = shift(n, int(command[1]))
#     elif command[0] == 'sumPairs':
#         n = [int(x) for x in n]
#         n = [sum(n[i:i+2]) for i in range(0, len(n), 2)]
#     elif command[0] == 'print':
#         print([int(x) for x in n])
#         que = False

# # 7. Sum Reversed Numbers
# n = input().split(' ')
# result = 0
# for i in n:
#     t = int(i[::-1])
#     result += t
# print(result)

# # 8. Bomb Numbers
# n = input().split(' ')
# command = input().split(' ')
# command_number, command_power = command[0], int(command[1])
#
# for count, i in enumerate(n):
#     if i == command_number:
#         count_start = max(count - command_power, 0)
#         count_end = min(count + command_power, len(n) - 1)
#         del n[count_start:count_end + 1]
#
# print(sum([int(x) for x in n]))