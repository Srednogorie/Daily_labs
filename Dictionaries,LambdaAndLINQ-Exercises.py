# # 1. Exercises: Dictionaries, Lambda and LINQ
# # 2. Phonebook
# n = input().split(' ')
# d = {}
#
# while n[0] != 'END':
#     if n[0] == 'A':
#         d[n[1]] = n[2]
#     elif n[0] == 'S':
#         if n[1] in d:
#             print('{} -> {}'.format(n[1], d[n[1]]))
#         else:
#             print('Contact {} does not exist.'.format(n[1]))
#     n = input().split(' ')

# # 3.  Phonebook Upgrade
# n = input().split(' ')
# d = {}
#
# while n[0] != 'END':
#     if n[0] == 'A':
#         d[n[1]] = n[2]
#     elif n[0] == 'S':
#         if n[1] in d:
#             print('{} -> {}'.format(n[1], d[n[1]]))
#         else:
#             print('Contact {} does not exist.'.format(n[1]))
#     elif n[0] == 'ListAll':
#         for key, value in sorted(d.items()):
#             print('{} -> {}'.format(key, value))
#     n = input().split(' ')

# # 3. A Miner Task
# n = input()
# resource, quntity, count, que = [], [], 1, False
#
# while n != 'stop':
#     if count % 2 != 0:
#         if n in resource:
#             ind = resource.index(n)
#             que = True
#         else:
#             resource.append(n)
#     else:
#         if que is True:
#             quntity[ind] += int(n)
#             que = False
#         else:
#             quntity.append(int(n))
#     count += 1
#     n = input()
#
# d = dict(zip(resource, quntity))
#
# for key, value in d.items():
#     print('{} -> {}'.format(key, value))

# # 4. Fix Emails
# n = input()
# name, email, count = [], [], 1
#
# while n != 'stop':
#     if count % 2 != 0:
#         name.append(n)
#         numm = name.index(n)
#     else:
#         if n.endswith('.us') or n.endswith('.uk'):
#             del name[numm]
#         else:
#             email.append(n)
#     count += 1
#     n = input()
#
# d = dict(zip(name, email))
#
# for key, value in d.items():
#     print('{} -> {}'.format(key, value))

# # 5. Hands of Cards
# import re
# n, d = input().split(': '), {}
#
# while n[0] != 'JOKER':
#     if n[0] in d:
#         d[n[0]] += n[1].split(', ')
#     else:
#         d[n[0]] = n[1].split(', ')
#     n = input().split(': ')
#
# numbers = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
# powers = {'S': 4, 'H': 3, 'D': 2, 'C': 1}
# for key, value in d.items():
#     result = 0
#     for i in list(set(value)):
#         n = re.match(r'([0-9JQKA]+)([SHDC])', i)
#         try:
#             result += int(n.group(1)) * powers[n.group(2)]
#         except:
#             result += numbers[n.group(1)] * powers[n.group(2)]
#     value.append(result)
#
# for a, b in d.items():
#     print('{}: -> {}'.format(a, b[-1]))

# # 6. * User Logs
# n = input().split(' ')
# d = {}
#
# while n[0] != 'end':
#     user = n[2].split('=')[1]
#     ip = n[0].split('=')[1]
#     if user in d:
#         if ip in d[user]:
#             d[user][ip] += 1
#         else:
#             d[user][ip] = 1
#     else:
#         d[user] = {}
#         d[user][ip] = 1
#     n = input().split(' ')
#
# for key, value in sorted(d.items()):
#     count = 0
#     print('{}:'.format(key))
#     for a, b in value.items():
#         print('{} => {}'.format(a, b), end='')
#         count += 1
#         if count < len(value):
#             print(', ', end='')
#         else:
#             print('.')

# # 7. * Population Counter
# n = input().split('|')
# d = {}
# t = {}
# # d = {'Bulgaria': {'Sofia': 1, 'Veliko Tarnovo': 2}, 'UK': {'London': 4}, 'Italy': {'Rome': 3}}
# # t = {'Bulgaria': 3, 'UK': 4, 'Italy': 3}
#
# while n[0] != 'report':
#     citi = n[0]
#     country = n[1]
#     count = n[2]
#     if country in d:
#         d[country][citi] = int(count)
#         t[country] = sum(d[country].values())
#     else:
#         d[country] = {}
#         d[country][citi] = int(count)
#         t[country] = sum(d[country].values())
#     n = input().split('|')
#
# t_sorted_list = sorted(t, key=t.get, reverse=True) # Sort by value. Return list of keys
# for i in t_sorted_list:
#     print('{} (total population: {})'.format(i, t[i]))
#     d_sorted_list = sorted(d[i], key=d[i].get, reverse=True)
#     for s in d_sorted_list:
#         print('=>{}: {}'.format(s, d[i][s]))
#
# # print(d)
# # print(t)

# # 8. * Logs Aggregator
# n = int(input())
# d, t = {}, {}
# # d = {'peter': ['192.168.0.11', '10.10.17.35', '10.10.17.34'], 'alex': ['10.10.17.33', '212.50.118.81']}
# # t = {'peter': 303, 'alex': 62}
#
# for i in range(n):
#     s = input().split(' ')
#     if s[1] in d:
#         if s[0] in d[s[1]]:
#             pass
#         else:
#             d[s[1]].append(s[0])
#         t[s[1]] += int(s[2])
#     else:
#         d[s[1]] = [s[0]]
#         t[s[1]] = int(s[2])
#
# for key, value in sorted(t.items()):
#     print('{}: {}'.format(key, value), end=' ')
#     print('[', end='')
#     print(*sorted(d[key]), sep=', ', end='')
#     print(']')

# # 9. * Legendary Farming
# k, j, que = {'shards': 0, 'fragments': 0, 'motes': 0}, {}, True
#
#
# def calculate(pair):
#     if i[1].lower() == 'shards' or i[1].lower() == 'fragments' or i[1].lower() == 'motes':
#         k[i[1].lower()] += int(i[0])
#         for key, value in k.items():
#             if value >= 250:
#                 if key == 'shards':
#                     print('Shadowmourne obtained!')
#                 elif key == 'fragments':
#                     print('Valanyr obtained!')
#                 elif key == 'motes':
#                     print('Dragonwrath obtained!')
#                 k[key] -= 250
#                 global que
#                 que = False
#     else:
#         if i[1].lower() in j:
#             j[i[1].lower()] += int(i[0])
#         else:
#             j[i[1].lower()] = int(i[0])
#
#
# while que is True:
#     n = input().split(' ')
#     tupled = zip(n[0::2], n[1::2])
#     for i in tupled:
#         result = calculate(i)
#         if que is False:
#             break
#
# sorted_k = [v[0] for v in sorted(k.items(), key=lambda kv: (-kv[1], kv[0]))] # Sotr by value, then if keys with same
#                                                                              # values sort them alphabetically
# for s in sorted_k:
#     print('{}: {}'.format(s, k[s]))
# for a, b in sorted(j.items()):
#     print('{}: {}'.format(a, b))

# # 10. ** Сръбско Unleashed
# n = input()
# venues = []
# singers = {}
#
# while n != 'End':
#     validate = n.split(' ')
#     if len(validate) < 4:
#         n = input()
#         continue
#     first_spit = n.split(' @')
#     second_split = first_spit[1].split(' ')
#     money_for_line = int(second_split.pop(-1)) * int(second_split.pop(-1))
#     venu = ' '.join(second_split)
#
#     if venu in venues:
#         if first_spit[0] in singers[venu]:
#             singers[venu][first_spit[0]] += money_for_line
#         else:
#             singers[venu][first_spit[0]] = money_for_line
#     else:
#         venues.append(venu)
#         singers[venu] = {}
#         singers[venu][first_spit[0]] = money_for_line
#
#     n = input()
#
# # venues = ['Sunny Beach', 'Belgrade']
# # singers = {'Sunny Beach': {'Lepa Brena': 87500, 'Ceca': 1148000, 'Mile Kitic': 73500, 'Saban Saolic': 4200000}, 'Belgrade': {'Ceca': 122500}}
# for i in venues:
#     print(i)
#     sorted_singers = sorted(singers[i], key=singers[i].get, reverse=True)
#     for s in sorted_singers:
#         print('#  {} -> {}'.format(s, singers[i][s]))

# 11. *** Dragon Army
n = int(input())
typee = []
name = {}

# typee = ['Gold']
# name = {'Gold': {'Zzazx': {'damage': 'null', 'health': '1000', 'armor': '10'}, 'Traxx': {'damage': '500', 'health': 'null', 'armor': '0'}, 'Xaarxx': {'damage': '250', 'health': '1000', 'armor': 'null'}, 'Ardrax': {'damage': '100', 'health': '1055', 'armor': '50'}}}

for i in range(n):
    s = input().split(' ')

    if s[0] in typee:
        name[s[0]][s[1]] = {}
        name[s[0]][s[1]]['damage'] = s[2]
        name[s[0]][s[1]]['health'] = s[3]
        name[s[0]][s[1]]['armor'] = s[4]
    else:
        typee.append(s[0])
        name[s[0]] = {}
        name[s[0]][s[1]] = {}
        name[s[0]][s[1]]['damage'] = s[2]
        name[s[0]][s[1]]['health'] = s[3]
        name[s[0]][s[1]]['armor'] = s[4]

for y in typee:
    for j, m in name[y].items():
        for k, v in m.items():
            if k == 'health' and v == 'null':
                name[y][j][k] = 250
            elif k == 'damage' and v == 'null':
                name[y][j][k] = 45
            elif k == 'armor' and v == 'null':
                name[y][j][k] = 10

for t in typee:
    mean_damage, mean_health, mean_armor = 0, 0, 0
    for p, h in name[t].items():
        mean_damage += int(h['damage'])
        mean_health += int(h['health'])
        mean_armor += int(h['armor'])
    print('{0}::({1:.2f}/{2:.2f}/{3:.2f})'.format(t, mean_damage/len(name[t]), mean_health/len(name[t]),
                                                  mean_armor/len(name[t])))
    sorted_dragons = sorted(name[t])
    for r in sorted_dragons:
        print('-{} -> {}: {}, {}: {}, {}: {}'.format(r, 'damage', name[t][r]['damage'], 'health',
                                                     name[t][r]['health'], 'armor', name[t][r]['armor']))

# print(typee)
# print(name)
# print(sorted_dragons)
