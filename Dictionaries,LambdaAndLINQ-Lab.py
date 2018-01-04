# from collections import Counter
# n = input().split(' ')
#
# result = sorted(Counter(n).items())
# for key, value in result:
#     print('{} -> {}'.format(key, value))

# # 3. Odd Occurrences
# from collections import Counter
# n = input().split(' ')
# n = [x.lower() for x in n]
#
# result = Counter(n)
#
# final = []
# for key, value in result.items():
#     if value % 2 != 0:
#         final.append(key)
#
# print(*final, sep=', ')

# # 6. Short Words Sorted
# import re
# n = input()
# result = [x.lower() for x in re.findall(r'([\w\'#-]+)', n) if len(x) < 5]
# result = list(set(result))
# print(*sorted(result), sep=', ')

# 7. Fold and Sum
from operator import add
n = input().split(' ')
n = [int(x) for x in n]

numm = int((len(n) / 2) / 2)

left, right, center = n[:numm][::-1], n[-numm:][::-1], n[numm:-numm]
left_right = left + right

print(*map(add, left_right, center), sep=' ')
