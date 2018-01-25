# 1. Lab: Regular Expressions (RegEx)
# # 2. Match Full Name
# import re
# n = input()
#
# result = re.finditer(r'( |^)([A-Z][a-z]* [A-Z][a-z]*)', n)
# array = [x.group(2) for x in result]
# print(*array, sep=' ')
#
# # Ivan Ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Test Testov, Ivan	Ivanov
# # Ivan Ivanov Test Testov

# # 3. Match Phone Number
# import re
# n = input()
# k = re.compile(r'(?:(?<=^)|(?<= ))([+][3][5][9])([ -])(2)(\2)(\d{3})([ -])(\d{4})\b')
# result = k.finditer(n)
# #result = re.finditer(r'(?:(?<=^)|(?<= ))([+][3][5][9])([ -])(2)(\2)(\d{3})([ -])(\d{4})(?= |,|$)', n)
# array = [x.group(0) for x in result]
# print(*array, sep=', ')
#
# # +359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222
# # +359 2 222 2222, +359-2-222-2222

# # 4. Match Hexadecimal Numbers
# import re
# n = input()
# k = re.compile(r'\b(?:0x)?[0-9A-F]+\b')
# result = k.finditer(n)
# array = [x.group(0) for x in result]
# print(*array, sep=' ')
#
# # 1F 0xG 0x1F G 0x4G 4G 0xAB 0xFG FG 0x10   10 AB  FF
# # 1F 0x1F 0xAB 0x10 10 AB FF

# # 5. Match Dates
# import re
# n = input()
# # k = re.compile(r'\b(\d{2})([-./])([A-Z][a-z]{2})(\2)(\d{4})\b')
# result = re.findall(r'\b(\d{2})([-./])([A-Z][a-z]{2})(\2)(\d{4})\b', n)
#
# for i in result:
#     print('Day: {}, Month: {}, Year: {}'.format(i[0], i[2], i[4]))
#
# 13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
# Day: 13, Month: Jul, Year: 1928
# Day: 10, Month: Nov, Year: 1934
# Day: 25, Month: Dec, Year: 1937

# # 6. Match Numbers
# import re
# n = input()
# k = re.compile(r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))')
# result = k.finditer(n)
# array = [x.group(0) for x in result]
#
# print(*array, sep=' ')
#
# # 1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5
# # 1 -1 123 -123 123.456 -123.456

# 7. Replace <a> Tag
