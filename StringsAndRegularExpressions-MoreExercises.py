# 1. More Exercises: Strings and Regular Expressions
# # 2. Censorship
# import re
# word = input()
# sentence = input()
#
# num = len(word)
# regex = re.compile(r'({})'.format(word))
#
# new_sentence = re.sub(regex, '*' * num, sentence)
#
# print(new_sentence)
#
# Java
# I love **** and ****Script, but I hate Rxjava

# # 3. Email Me
# import re
# n = input()
# regex = re.compile(r'(.*)(?=@)(?:@)(?<=@)(.*)')
#
# k = regex.finditer(n)
#
# for i in k:
#     num = len(i.group(1)) - len(i.group(2))
#     if num >= 0:
#         print('Call her!')
#     else:
#         print('She is not the one.')
#
# maria@abv.bg
# She is not the one.
# gergana.ivanova@yahoo.com
# Call her!

# 4. Karate Strings
import re
n = input()
regex = re.compile(r'(?<=>)(\d)*')
numm = len(regex.findall(n))

working_string = n
extra_power = 0
for i in range(numm):
    result = re.search(r'(?<=>)(\d)+(?=>|[a-zA-Z])', n)
    power = int(result.group(0)) + extra_power
    partial = list(working_string[result.span()[0]:result.span()[0] + power])
    for k in partial[:]:
        if k != '>':
            partial.remove(k)
        else:
            break
    final_partial = ''.join(partial)
    working_string = working_string[:result.span()[0]] + final_partial + working_string[result.span()[0] + power:]
    extra_power = len(partial)
    n = working_string
print(working_string)

# # 5. * Morse Code Upgraded
# import re
# n = input().split('|')
# total = 0
# string = ''
# for i in n:
#     for k in i:
#         if k == '0':
#             total += 3
#         elif k == '1':
#             total += 5
#     regex = re.compile(r'(\d)\1*')
#     k = regex.finditer(i)
#     for m in k:
#         if len(m.group(0)) > 1:
#             total += len(m.group(0))
#     string += chr(total)
#     total = 0
# print(string)
#
# 01010101010101011|111001111100001111110|111001111100001111110|000011000011111010110|110010011010101011100|11110000000100110011010101|110001100101110101101
# Goodbye

# # 6. Only Letters
# import re
# n = input()
# regex = re.compile(r'(\d+)(?=[a-zA-Z])([a-zA-Z])')
# k = regex.findall(n)
#
# for i in k:
#     n = n.replace(i[0], i[1])
#
# print(n)
#
# ChangeThis12andThis56k
# ChangeThisaandThiskk
# 1Beware72ForThe4End88888
# BBewareFForTheEEnd88888

# # 7. Email Statistics
# import re
# n = int(input())
# regex = re.compile(r'([a-zA-Z]{5,})(?=@)@([a-z]{3,})(.com|.bg|.org)')
# d = {}
# for i in range(n):
#     x = input()
#     validation = re.match(regex, x)
#     try:
#         string = validation.group(0).split('@')
#         if string[1] in d:
#             d[string[1]].append(string[0])
#         else:
#             d[string[1]] = []
#             d[string[1]].append(string[0])
#     except:
#         continue
# s = sorted(d, key=lambda k: len(d[k]), reverse=True)
# for z in s:
#     print('{}:'.format(z))
#     for f in d[z]:
#         print('### {}'.format(f))
#
# 5
# Georgi@abv.bg
# Petran@gmail.com
# Vladi@gmail.com
# super_man@abv.bg
# superMan@abv.bg
# abv.bg:
# ### Georgi
# ### superMan
# gmail.com:
# ### Petran
# ### Vladi

# # 8. Hideout !!!!!!!!!!!!!!!!!!! Check !!!!!!!!!!!
# import re
# string = input()
# clue = True
# total = 0
#
# while clue is True:
#     intellig = input().split(' ')
#     check_string = string[:int(intellig[1])]
#     for enum, value in enumerate(check_string):
#         if value == intellig[0]:
#             numm = enum
#             final_string = string[numm:]
#             total += numm
#             regex = re.compile(r'(.)\1*')
#             result = re.match(regex, final_string)
#             print(len(result.group(0)))
#             print('Hideout found at index {} and it is with size {}!'.format(total, len(result.group(0))))
#             clue = False
#             break
#     string = string[int(intellig[1]):]

# # 9. * Mines
# import re
# n = input()
# regex = re.compile(r'(<)(?=[a-zA-z]*)([a-zA-Z]{2})(>)')
# k = regex.finditer(n)
#
# working_string = n
#
# for i in k:
#     #print(i.group(2), i.span()[0], i.span()[1])
#     numm_letters = abs(ord(i.group(2)[0]) - ord(i.group(2)[1]))
#     start = i.span()[0] - numm_letters
#     end = i.span()[1] + numm_letters
#     underscores = abs(start - end)
#     working_string = working_string[:start] + '_' * underscores + working_string[end:]
# print(working_string)
#
# bewareOf<AF>TheMines
# bew______________nes
# TwoMin<ag>esWillBeHe<HH>reMuchDangerous
# ________________BeHe____reMuchDangerous