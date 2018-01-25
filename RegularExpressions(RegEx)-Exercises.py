# 1. Exercises: Regular Expressions (RegEx)
# # 1. Extract Emails
# import re
# n = input()
# regex = re.compile(r"([a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*(@|\sat\s)"
#                     "(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")
# k = regex.findall(n)
# for i in k:
#     print(i[0])
#
# Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de.
# steve.parker@softuni.de

# # 2. Extract Sentences by Keyword
# import re
# text = input()
# word = input() # to
# regex = re.compile(r'([A-Z][^.!?]*? to [^.!?]*)(?=[.!?])')
# k = regex.findall(text)
#
# for i in k:
#     print(i)
#
# Welcome to SoftUni! You will learn programming, algorithms, problem solving and software technologies. You need to allocate for study 20-30 hours weekly. Good luck! I am fan of Motorhead. To be or not to be - that is the question. TO DO OR NOT?
# Welcome to SoftUni
# You need to allocate for study 20-30 hours weekly
# To be or not to be - that is the question

# # 3. Camera View
# import re
# skip_take = input().split(' ')
# view = input()
# regex = re.compile(r'(?<=[|][<])(\w+)')
# k = regex.findall(view)
# array = [i[int(skip_take[0]):int(skip_take[1]) + int(skip_take[0])] for i in k]
# print(*array, sep=', ')
#
# # 9 7
# # GreatBigSea|<uglyStuffHawaii|<boriiiingKilauea
# # Hawaii, Kilauea

# # 4. Weather
# import re
# n = input()
# d = {}
#
# while n != 'end':
#     regex = re.compile(r'([A-Z]{2})-?([0-9]{1,2}.[0-9]{1,2})([A-Za-z]+)(?=\|)')
#     k = regex.findall(n)
#     if len(k) > 0:
#         d[k[0][0]] = {}
#         d[k[0][0]]['temp'] = k[0][1]
#         d[k[0][0]]['cond'] = k[0][2]
#     n = input()
#
# s = sorted(d, key=lambda x: (d[x]['temp']))
# for x in s:
#     print('{} => {:.2f} => {}'.format(x, float(d[x]['temp']), d[x]['cond']))
#
# PB23.41Rainy|ASDASD
# SDASCA20.21sUNNY|SDASD
# asdaCA22.5rainy|sada
# CA23.41cloydy
# end
# CA => 12.41 => Rainy
# YA => 21.51 => sunny
# PA => 31.21 => cloudy

# # 5. Key Replacer
# import re
# key_string = input()
# text_string = input()
#
# key_string = key_string.replace('|', ' ').replace('<', ' ').replace('\\', ' ').split(' ')
# key_one = key_string[0]
# key_two = key_string[-1]
#
# regex = re.compile(r'{}(?!{})(.*?){}'.format(key_one, key_two, key_two))
# k = regex.findall(text_string)
#
# final_string = ''
# for i in k:
#     final_string += i
# print(final_string)
#
# start<213asfaas|end
# saaastarthelloendsdarstartFromTheOtherenddvsefdsfstartSideend

# # 6. * Valid Usernames
# import re
# n = input()
# result = re.findall(r'\b([A-Za-z]\w{2,24})\b', n)
#
# best = 0
# list = []
# counter = 0
#
# for i in range(len(result) - 1):
#     number = len(result[counter]) + len(result[counter + 1])
#     if number > best:
#         best = number
#         list = [result[counter], result[counter + 1]]
#     counter += 1
#
# for i in list:
#     print(i)
#
# ds3bhj y1ter/wfsdg 1nh_jgf ds2c_vbg\4htref
# wfsdg
# ds2c_vbg

# # 7. * Query Mess
# import re
# n = input()
#
# while n != 'END':
#     regex = re.compile(r'([^&=?\s]*)(?=\=)=(?<=\=)([^&=\s]*)')
#     result = regex.findall(n)
#
#     clean = re.compile(r'((%20|\+)+)')
#     d = {}
#     for i in result:
#         a = re.sub(clean, ' ', i[0]).strip()
#         b = re.sub(clean, ' ', i[1]).strip()
#         if a in d:
#             d[a].append(b)
#         else:
#             d[a] = []
#             d[a].append(b)
#
#     for key, value in d.items():
#         print(key + '=', end='')
#         print('[', end='')
#         print(*value, sep=', ', end='')
#         print(']', end='')
#     print()
#     n = input()
#
# foo=%20foo&value=+val&foo+=5+%20+203
# foo=[foo, 5 203]value=[val]

# # 8. *Use Your Chains, Buddy
# import re
# n = input()
#
# regex = re.compile(r'(?<=<p>)(.*?)(?=</p>)')
# k = re.findall(regex, n)
#
# clean = re.compile(r'([^a-z0-9])')
# k = [re.sub(clean, ' ', x) for x in k]
#
# final_list = []
# final_string = ''
# for i in k:
#     for m in i:
#         order = ord(m)
#         if 97 <= order <= 109:
#             letter = order + 13
#             final_string += chr(letter)
#         elif 110 <= order <= 122:
#             letter = order - 13
#             final_string += chr(letter)
#         else:
#             final_string += m
#     final_list.append(final_string)
#     final_string = ''
#
# final_list = [' '.join(x.split()) for x in final_list]
#
# print(*final_list)

# <html><head><title></title></head><body><h1>hello</h1><p>znahny!@#%&&&&****</p><div><button>dsad</button></div><p>grkg^^^^%%%)))([]12</p></body></html>
# manual text 12