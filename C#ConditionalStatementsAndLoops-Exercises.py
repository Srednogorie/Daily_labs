# # Problem 5. * Word in Plural
# string = input()
# if string.endswith('y'):
#     new_string = string.replace('y', 'ies')
#     print(new_string)
# elif string.endswith('o') or string.endswith('ch') or string.endswith('s') or string.endswith('sh') or \
#      string.endswith('x') or string.endswith('z'):
#     new_string = string + 'es'
#     print(new_string)
# else:
#     new_string = string + 's'
#     print(new_string)

# # Problem 11. Different Numbers
# import itertools
# a, b, listt = int(input()), int(input()), []
# for i in range(a, b+1):
#     listt.append(i)
# if len(listt) < 5:
#     print('No')
# else:
#     prod = itertools.product(listt, repeat=5)
#     for i in prod:
#         if a <= i[0] < i[1] < i[2] < i[3] < i[4] <= b:
#             #print(''.join(map(str, sum(i, ()))), end=' ')
#             print(' '.join(map(str, sum((i,), ()))))

# # Problem 12. Test Numbers
# import itertools
# a, b, num, listt, listt1, summ, counter = int(input()), int(input()), int(input()), [], [], 0, 0
# for i in range(1, a+1):
#     listt.append(i)
# listt.reverse()
# for i in range(1, b+1):
#     listt1.append(i)
# prod = itertools.product(listt, listt1, repeat=1)
#
# for i in prod:
#     total = 3 * (i[0] * i[1])
#     summ += total
#     counter += 1
#     if summ >= num:
#         break
# print('{} combinations'.format(counter))
# if summ >= num:
#     print('Sum: {} >= {}'.format(summ, num))
# else: print('Sum: {}'.format(summ))

# # Problem 13. Game of Numbers
# import itertools
# a, b, magic, listt, counter, nishan = int(input()), int(input()), int(input()), [], 0, 0
# for i in range(a, b+1):
#     listt.append(i)
# prod = itertools.product(listt, repeat=2)
# for i in prod:
#     counter += 1
#     if i[0] + i[1] == magic:
#         print('Number found! {} + {} = {}'.format(i[1], i[0], magic))
#         nishan += 1
#         break
# if nishan == 0:
#     print('{} combinations - neither equals {}'.format(counter, magic))

# # Problem 14. * Magic Letter
# import itertools
# a, b, c, listt = input(), input(), input(), []
# for i in range(ord(a), ord(b)+1):
#     listt.append(chr(i))
# prod = itertools.product(listt, repeat=3)
# for j in prod:
#     if j[0] != c and j[1] != c and j[2] != c:
#         print(''.join(map(str, sum((j, ), ()))), end=' ')

# Problem 15. * Neighbour Wars
pesho_damage, gosho_damage, pesho_health, gosho_health, rund, game = int(input()), int(input()), 100, 100, 0, True

while game == True:
    if rund % 2 == 0:
        gosho_health -= pesho_damage
        if gosho_health <= 0:
            print('Pesho won in {}th round.'.format(rund + 1))
            game = False
            break
        print('Pesho used Roundhouse kick and reduced Gosho to {} health.'.format(gosho_health))
    else:
        pesho_health -= gosho_damage
        if pesho_health <= 0:
            print('Gosho won in {}th round.'.format(rund + 1))
            game = False
            break
        print('Gosho used Thunderous fist and reduced Pesho to {} health.'.format(pesho_health))
    rund += 1
    if rund % 3 == 0:
        gosho_health += 10
        pesho_health += 10