# Problem 1. Exercises: Strings and Text Processing
# # Problem 2. Convert from Base-10 to Base-N
# n = input().split(' ')
# base_n = int(n[0])
# base_10 = int(n[1])
#
#
# def to_str(n,base):
#    convertString = "0123456789ABCDEF"
#    if n < base:
#       return convertString[n]
#    else:
#       return to_str(n//base,base) + convertString[n%base]
#
# print(to_str(base_10,base_n))

# # Problem 3. Convert from Base-N to Base-10
# n = input().split(' ')
# to_base = int(n[0])
# number = n[1]
#
# def to_decimal(number, base):
#     return sum([int(character) * base ** index for index,character in enumerate(str(number)[::-1])])
#
# print(to_decimal(number, to_base))

# # Problem 4. Unicode Characters
# n = input()
# n = n.encode()
#
# array = []
# new_array = []
#
# for i in n:
#     array.append(str(hex(i)))
#
# for m in array:
#     new = m.replace('x', '0')
#     new_array.append(new)
#
# print('\\u', end='')
# print(*new_array, sep='\\u')

# # Problem 5. Character Multiplier
# n = input().split(' ')
# first_s = n[0]
# second_s = n[1]
#
# def multiply_characters(str_one, str_two):
#     list_one = [ord(x) for x in str_one]
#     list_two = [ord(x) for x in str_two]
#     if len(list_one) == len(list_two):
#         list_three = []
#     else:
#         if len(list_one) > len(list_two):
#             list_three = list_one[len(list_two):]
#         else:
#             list_three = list_two[len(list_one):]
#
#     final_list = [a*b for a,b in zip(list_one, list_two)]
#
#     print(sum(final_list) + sum(list_three))
#
# multiply_characters(first_s, second_s)

# Problem 6. Magic Exchangeable Words
n = input().split(' ')

def exchangable(word_one, word_two):
    maper = dict(zip(word_one, word_two))
    additional = ''
    que = True
    if len(word_one) < len(word_two):
        additional = word_two[len(word_one):]
        word_two = word_two[:len(word_one)]
    elif len(word_one) > len(word_two):
        additional = word_one[len(word_two):]
        word_one = word_one[:len(word_two)]
        que = False

    final_string = ''
    for i in word_one:
        final_string += maper[i]

    if len(additional) > 0:
        if que is True:
            for j in additional:
                if j in maper.values():
                    final_string += j
            if final_string == word_two + additional:
                print('true')
            else:
                print('false')
        else:
            if all(x in maper.keys() for x in additional):
                print('true')
            else:
                print('false')
    else:
        if final_string == word_two:
            print('true')
        else:
            print('false')

exchangable(n[0], n[1])

# # Problem 7. Sum Big Numbers
# a = int(input())
# b = int(input())
#
# print(a + b)

# # Problem 8. Multiply Big Number
# a = int(input())
# b = int(input())
#
# print(a * b)

# # Problem 9. *Letters Change Numbers
# import math
# n = input().split(' ')
# n = [x for x in n if x]
# alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
#
# total = 0
# for i in n:
#     num = int(i[1:-1])
#     if i[0].isupper():
#         divisor = alphabet_upper.index(i[0]) + 1
#         num /= divisor
#     elif i[0].islower():
#         multiplier = alphabet_lower.index(i[0]) + 1
#         num *= multiplier
#
#     if i[-1].isupper():
#         subtractor = alphabet_upper.index(i[-1]) + 1
#         num -= subtractor
#     elif i[-1].islower():
#         addtor = alphabet_lower.index(i[-1]) + 1
#         num += addtor
#
#     total += num
#
# print('{0:.2f}'.format(total))

# # Problem 10. ** Melrah Shake
# string = input()
# pattern = input()
#
# first = string.find(pattern)
# last = string.rfind(pattern)
#
# while first != -1 and last != -1:
#     len_pattern = len(pattern)
#     string = string[:first] + string[first + len_pattern:]
#     string = string[:last - len_pattern] + string[last:]
#
#     index_patern = int(len_pattern / 2)
#     pattern = pattern[:index_patern] + pattern[index_patern + 1:]
#
#     first = string.find(pattern)
#     last = string.rfind(pattern)
#
#     print('Shaked it.')
#
# print('No shake.')
# print(string)