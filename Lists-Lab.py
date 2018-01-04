# # 4. Sum Adjacent Equal Numbers
# n, lista = input(), []
# s = n.split(' ')
# for k in s:
#     try:
#         lista.append(int(k))
#     except:
#         lista.append(float(k))
#
#
# def calculate(lista):
#     for count, i in enumerate(lista):
#         numm = i
#         try:
#             if numm == lista[count + 1]:
#                 lista[count] = numm * 2
#                 lista.remove(lista[count + 1])
#                 calculate(lista)
#         except:
#             break
#     return lista
#
#
# result = calculate(lista)
# for i in result:
#     print(i, end=' ')

# # 5. Split by Word Casing
# import re
# n = input()
# result = re.findall(r"[\w#]+", n)
# lower, uper, mixed = [], [], []
# for i in result:
#     if i.islower():
#         lower.append(i)
#     elif i.isupper():
#         uper.append(i)
#     else:
#         mixed.append(i)
# print('Lower-case:', end=' ')
# for j in lower:
#     print(j, end=' ')
# print()
# print('Mixed-case:', end=' ')
# for k in mixed:
#     print(k, end=' ')
# print()
# print('Upper-case:', end=' ')
# for s in uper:
#     print(s, end=' ')

# 8. Count Numbers
from collections import Counter
n, lista = input(), []
s = n.split(' ')
for j in s:
    lista.append(int(j))

result = Counter(lista)
seted = sorted(list(set(lista)))
# print(result)
# print(seted)

for i in seted:
    print('{} -> {}'.format(i, result[i]))