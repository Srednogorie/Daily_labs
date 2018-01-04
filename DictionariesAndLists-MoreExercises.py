# Problem 1. More Exercises: Dictionaries and Lists
# # Problem 2. Sort Times
# n = input().split(' ')
# print(*sorted(n), sep=', ')

# # Problem 3. Odd Filter
# n = input().split(' ')
# n = list(map(int, n))
#
# def remove_odd(array):
#     return [x for x in array if x % 2 == 0]
#
# result = remove_odd(n)
# av = sum(result) / float(len(result))
#
# final = []
#
# for i in result:
#     if i > av:
#         i += 1
#         final.append(i)
#     elif i <= av:
#         i -= 1
#         final.append(i)
#
# print(*final, sep=' ')

# # Problem 4. Immune System
# initial_health = int(input())
# current_health = initial_health
# virus = input()
# virus_list = []
# seconds_to_defeat = []
# que = False
#
# while virus != 'end':
#     virus_strength = 0
#     if virus in virus_list:
#         for i in virus:
#             virus_strength += ord(i)
#         final_virus_strength = int(virus_strength / 3)
#         time_in_seconds_to_defeat = int(final_virus_strength * len(virus) / 3)
#     else:
#         for i in virus:
#             virus_strength += ord(i)
#         final_virus_strength = int(virus_strength / 3)
#         time_in_seconds_to_defeat = int(final_virus_strength * len(virus))
#         virus_list.append(virus)
#
#     seconds_to_defeat.append(time_in_seconds_to_defeat)
#     if time_in_seconds_to_defeat > current_health:
#         print('Virus {}: {} => {} seconds'.format(virus, final_virus_strength, time_in_seconds_to_defeat))
#         print('Immune System Defeated.')
#         que = True
#         break
#     else:
#         print('Virus {}: {} => {} seconds'.format(virus, final_virus_strength, time_in_seconds_to_defeat))
#         minutes = time_in_seconds_to_defeat // 60
#         seconds = time_in_seconds_to_defeat % 60
#         print('{} defeated in {}m {}s.'.format(virus, minutes, seconds))
#         print('Remaining health: {}'.format(current_health - time_in_seconds_to_defeat))
#         current_health -= time_in_seconds_to_defeat
#         current_health += int(current_health * 0.20)
#         if current_health > initial_health:
#             current_health = initial_health
#
#     virus = input()
#
# if que is False:
#     print('Final Health: {}'.format(current_health))
#
# # print(final_virus_strength)
# # print(seconds_to_defeat)
# # print(virus_list)
# # print(current_health)

# # Problem 6. Parking Validation
# n = int(input())
# parking_users = {}
#
# for i in range(n):
#     command = input().split(' ')
#     if command[0] == 'register':
#         if command[1] in parking_users:
#             print('ERROR: already registered with plate number {}'.format(parking_users[command[1]]))
#             continue
#
#         if len(command[2]) == 8 and command[2][0].isupper() and command[2][1].isupper() and \
#            command[2][2].isdigit() and command[2][3].isdigit() and command[2][4].isdigit() and \
#            command[2][5].isdigit() and command[2][6].isupper() and command[2][7].isupper():
#             pass
#         else:
#             print('ERROR: invalid license plate {}'.format(command[2]))
#             continue
#
#         if command[2] in parking_users.values():
#             print('ERROR: license plate {} is busy'.format(command[2]))
#             continue
#
#         parking_users[command[1]] = command[2]
#         print('{} registered {} successfully'.format(command[1], command[2]))
#     elif command[0] == 'unregister':
#         if command[1] not in parking_users:
#             print('ERROR: user {} not found'.format(command[1]))
#             continue
#
#         parking_users.pop(command[1])
#         print('user {} unregistered successfully'.format(command[1]))
#
# for a, b in parking_users.items():
#     print('{} => {}'.format(a, b))

# # Problem 7. Byte Flip
# n = input().split(' ') # Split the list
# n = [e for e in n if len(e) == 2] # Remove all lens different then 2
# n = [x[::-1] for x in n] # Reverse all the strings in the list
# n = n[::-1] # Reverse the entire list
#
# for i in n:
#     print(bytearray.fromhex(i).decode(), end='') # From hex to string

# # Problem 8. * Take/Skip Rope
# n = input()
# numbers_list = []
#
# for i in n:
#     if i.isdigit():
#         numbers_list.append(i)
#
# new_n = ''.join([i for i in n if not i.isdigit()])
#
# count = 0
# take_list = []
# skip_list = []
#
# for j in numbers_list:
#     if count % 2 == 0:
#         take_list.append(j)
#     else:
#         skip_list.append(j)
#     count += 1
#
# take_list = [int(x) for x in take_list]
# skip_list = [int(x) for x in skip_list]
#
# final_string = ''
# start = 0
#
# for m in range(len(take_list)):
#     end = start + take_list[m]
#     string = new_n[start:end]
#     final_string += string
#
#     start += skip_list[m] + take_list[m]
#
# print(final_string)
