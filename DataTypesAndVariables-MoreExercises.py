# # Problem 10. Sum of Chars
# n = int(input())
# summ = 0
# for i in range(n):
#     a = input()
#     summ += ord(a)
# print('The sum equals: {}'.format(summ))

# # Problem 11. String Concatenation
# delim, e_o, n = input(), input(), int(input())
# strr, lista = '', []
# for i in range(n):
#     nmm = input()
#     lista.append(nmm)
# if e_o == 'even':
#     strr = strr + lista[1] + delim + lista[3]
# elif e_o == 'odd':
#     strr = strr + lista[0] + delim + lista[2]
# print(strr)

# # Problem 14. * Boat Simulator
# first_boat, second_boat, n = ord(input()), ord(input()), int(input())
# score_first, score_second, que = 0, 0, 0
# for i in range(1, n + 1):
#     speed = input()
#     if speed == 'UPGRADE':
#         first_boat += 3
#         second_boat += 3
#
#     if i % 2 == 1:
#         score_first += len(speed)
#     elif i % 2 == 0:
#         score_second += len(speed)
#
#     if score_first >= 50:
#         que = 1
#         print(chr(first_boat))
#         break
#     elif score_second >= 50:
#         que = 1
#         print(chr(second_boat))
#         break
#
# if que == 0:
#     if score_first > score_second:
#         print(chr(first_boat))
#     else:
#         print(chr(second_boat))

# Problem 15. * Balanced Brackets
n, open, close = int(input()), 0, 0
for i in range(n):
    simb = input()
    if simb == '(':
        open += 1
    elif simb == ')':
        close += 1
    else:
        continue

if open == close:
    print('BALANCED')
else:
    print('UNBALANCED')