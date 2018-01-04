# # 6. Special Numbers
# n = int(input())
# def sum_digits(number):
#     s = 0
#     while number:
#         s += number % 10
#         number //= 10
#     return s
#
# for i in range(1, n + 1):
#     result = sum_digits(i)
#     if result == 5 or result == 7 or result == 11:
#         print('{} -> True'.format(i))
#     else:
#         print('{} -> False'.format(i))

# # 7. Triples of Latin Letters
# import itertools
# n, lista = int(input()), []
# for i in range(ord('a'), ord('a') + n):
#     lista.append(chr(i))
# prod = itertools.product(lista, repeat=3)
# for j in prod:
#     print(''.join(j))

# # 9. Refactor Volume of Pyramid
# length, width, height = float(input('Length: ')), float(input('Width: ')), float(input('Height: '))
# volume = (length * width * height) / 3
# print('Pyramid Volume: {0:.2f}'.format(volume))