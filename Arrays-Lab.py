# # 2. Day of Week
# day = int(input())
# day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#
# if 0 < day <= 7:
#     print(day_of_week[day-1])
# else:
#     print('Invalid Day!')

# # 3. Reverse an Array of Integers
# n, lista = int(input()), []
# for i in range(n):
#     numb = int(input())
#     lista.append(numb)
# for j in reversed(lista):
#     print(j, end=' ')

# # 4. Last K Numbers Sums Sequence
# n, k, lista = int(input()), int(input()), [1]
# start, end = 0, k
# for i in range(n - 1):
#     if len(lista) < k + 1:
#         lista.append(sum(lista[start:end]))
#     elif len(lista) >= k + 1:
#         start += 1
#         end += 1
#         lista.append(sum(lista[start:end]))
# for s in lista:
#     print(s, end=' ')

# # 5. Triple Sum
# n, numbers, que = input(), [], False
# s = n.replace(' ', '')
# for i in s:
#     numbers.append(int(i))
#
# for count, j in enumerate(numbers):
#     for k in numbers[count + 1:]:
#         if (j + k) in [e for e in numbers if e not in (j, k)]:
#             result = j + k
#             print('{} + {} == {}'.format(j, k, result))
#             que = True
#
# if que is False:
#     print('No')

# # 9. Condense Array to Number
# n, lista = input(), []
# s = n.split(' ')
# for k in s:
#     lista.append(int(k))
# new_lista = []
# count, que = 0, True
#
# while que is True:
#     for i in range(len(lista) - 1):
#         numb = lista[count] + lista[count + 1]
#         new_lista.append(numb)
#         count += 1
#     lista = new_lista
#     new_lista = []
#     count = 0
#
#     if len(lista) == 1:
#         print(lista[0])
#         que = False

# 10. Extract Middle 1, 2 or 3 Elements
n, lista = input(), []
s = n.split(' ')
for k in s:
    lista.append(int(k))

if len(lista) == 1:
    print('{{ {} }}'.format(lista[0]))
elif len(lista) % 2 == 0:
    numm = int((len(lista) - 2) / 2)
    print('{{ {}, {} }}'.format(lista[numm], lista[numm + 1]))
elif len(lista) % 2 == 1:
    numm = int((len(lista) - 2) / 2)
    print('{{ {}, {}, {} }}'.format(lista[numm], lista[numm + 1], lista[numm + 2]))
