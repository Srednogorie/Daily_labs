# # Problem 1. X
# n = int(input())
# inner_white, outer_white = n - 2, 0
# for i in range(int(n / 2)):
#     print(' ' * outer_white + 'x' + ' ' * inner_white + 'x')
#     outer_white += 1
#     inner_white -= 2
# print(' ' * outer_white + 'x')
# inner_white, outer_white = 1, int((n - 2)/2)
# for j in range(int(n / 2)):
#     print(' ' * outer_white + 'x' + ' ' * inner_white + 'x')
#     outer_white -= 1
#     inner_white += 2

# # Problem 2. Vapor Store
# valid_games = {'OutFall 4': 39.99, 'CS: OG': 15.99, 'Zplinter Zell': 19.99, 'Honored 2': 59.99,
#                'RoverWatch': 29.99, 'RoverWatch Origins Edition': 39.99}
# game = True
# initial_balance = float(input())
# current_balance = initial_balance
# cue = 0
# while game == True:
#     if current_balance == 0:
#         print('Out of money!')
#         cue = 1
#         break
#     game_to_buy = input()
#     if game_to_buy == 'Game Time':
#         game = False
#     else:
#         if game_to_buy in valid_games:
#             if valid_games[game_to_buy] > current_balance:
#                 print('Too Expensive')
#             else:
#                 print('Bought {}'.format(game_to_buy))
#                 current_balance = current_balance - valid_games[game_to_buy]
#         else:
#             print('Not Found')
# if cue == 0:
#     print('Total spent: ${0:.2f}. Remaining: ${1:.2f}'.format(initial_balance - current_balance, current_balance))


# # Problem 6. DNA Sequences
# import itertools
# n = int(input())
# dictt = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
# lista = []
# prod = itertools.product(dictt.keys(), repeat=3)
# for i in prod:
#     sumit = 0
#     for j in i:
#         sumit += dictt[j]
#     if sumit >= n:
#         mystring  = str(i).replace('(', '').replace(')', '').replace(', ', '').replace("'", '')
#         lista.append('O' + mystring + 'O')
#     else:
#         mystring = str(i).replace('(', '').replace(')', '').replace(', ', '').replace("'", '')
#         lista.append('X' + mystring + 'X')
# for i in range(int(len(lista)/4+1)):
#     print (' '.join(lista[i*4:(i+1)*4]) + '')

# # Problem 7. Training Hall Equipment
# budget = int(input())
# subtotal = 0
# num_items = int(input())
# for i in range(num_items):
#     product = input()
#     price = float(input())
#     quantiti = int(input())
#     subtotal += price * quantiti
#     if quantiti > 1:
#         print('Adding {0} {1}s to cart.'.format(quantiti, product))
#     else:
#         print('Adding {0} {1} to cart.'.format(quantiti, product))
# if budget >= subtotal:
#     print('Subtotal: ${0:.2f}'.format(subtotal))
#     print('Money left: ${0:.2f}'.format(budget - subtotal))
# else:
#     print('Subtotal: ${0:.2f}'.format(subtotal))
#     print('Not enough. We need ${0:.2f} more.'.format(abs(budget - subtotal)))

# Problem 8. * SMS Typing
len_mess = int(input())
message_list = []
alphabet = []
for m in range(ord('a'), ord('z') + 1):
    alphabet.append(chr(m))
for i in range(len_mess):
    letter = int(input())
    message_list.append(letter)
message = []
for j in message_list:
    if j == 0:
        message.append(' ')
    else:
        num_of_digits = len(str(j))
        main_digit = str(j)[0]
        if main_digit == '8' or main_digit == '9':
            offset = ((int(main_digit) - 2) * 3) + 1
        else:
            offset = (int(main_digit) - 2) * 3
        index = offset + num_of_digits - 1
        message.append(alphabet[index])
print(''.join(message))