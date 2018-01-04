# # Problem 4. Grab and Go
# array, n = input(), int(input())
# s = array.split(' ')
# result = list(map(int, s))
#
# try:
#     last_occurence = (len(result) -1) - list(reversed(result)).index(n)
#     print(sum(result[:last_occurence]))
# except:
#     print('No occurrences were found!')

# # Problem 6. Heists
# array = input()
# s = array.split(' ')
# prices = list(map(int, s))
# que = True
# total = 0
#
# while que is True:
#     heist, jewels, gold = input(), 0, 0
#     if heist != 'Jail Time':
#         ref = heist.split(' ')
#         h, e = ref[0], int(ref[1])
#         jewels += h.count('%')
#         gold += h.count('$')
#         income = ((jewels * prices[0]) + (gold * prices[1])) - e
#         total += income
#     else:
#         if total >= 0:
#             print('Heists will continue. Total earnings: {}.'.format(total))
#             que = False
#         else:
#             print('Have to find another job. Lost: {}.'.format(abs(total)))
#             que = False

# # Problem 7. Inventory Matcher
# product, quantyti, price = input(), input(), input()
# l_product, l_quantyti, l_price = product.split(' '), quantyti.split(' '), price.split(' ')
# l_quantyti, l_price = list(map(int, l_quantyti)), list(map(float, l_price))
#
# que = True
#
# while que is True:
#     info = input()
#     if info != 'done':
#         info_prod, info_quant = info.split(' ')[0], int(info.split(' ')[1])
#         numm = l_product.index(info_prod)
#         try:
#             if info_quant <= l_quantyti[numm]:
#                 l_quantyti[numm] -= info_quant
#                 total_price = info_quant * l_price[numm]
#                 print('{} x {} costs {:.2f}'.format(info_prod, info_quant, total_price))
#             else:
#                 print('We do not have enough {}'.format(info_prod))
#         except:
#             print('We do not have enough {}'.format(info_prod))
#     else:
#         que = False

# # Problem 9. * Jump Around
# inflow = input()
# inflow = inflow.split(' ')
# l_inflow = list(map(int, inflow))
#
# result_list = []
# result_list.append(l_inflow[0])
#
# left_check, right_check = True, True
#
# index_of_num = 0
# num = l_inflow[0]
#
# while left_check is True and right_check is True:
#     try:
#         result_list.append(l_inflow[index_of_num + num])
#         index_of_num += num
#         num = l_inflow[index_of_num]
#     except:
#         right_check = False
#         try:
#             result_list.append(l_inflow[index_of_num - num])
#             index_of_num -= num
#             num = l_inflow[index_of_num]
#         except:
#             left_check = False
#
# print(sum(result_list))

# Problem 9. * Jump Around
inflow = input()
inflow = inflow.split(' ')
l_inflow = list(map(int, inflow))

result = 0
index_of_num = 0

while index_of_num >= 0:
    if index_of_num < len(l_inflow):
        result += l_inflow[index_of_num]
        if index_of_num + l_inflow[index_of_num] < len(l_inflow):
            index_of_num += l_inflow[index_of_num]
        else:
            index_of_num -= l_inflow[index_of_num]
print(result)