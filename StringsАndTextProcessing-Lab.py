# 1. Lab: Strings and Text Processing
# # 2. Reverse string
# n = input()
# print(n[::-1])

# # 3. Count substring occurrences
# n = input().lower()
# look = input().lower()
#
# def occurrences(string, sub): # Count overlaping occurrences
#     count = start = 0
#     while True:
#         start = string.find(sub, start) + 1
#         if start > 0:
#             count+=1
#         else:
#             return count
#
# result = occurrences(n, look)
#
# print(result)

# # 4. Text filter
# forbiden = input().split(', ')
# text = input()
#
# for i in forbiden:
#     text = text.replace(i, '*' * len(i))
#
# print(text)

# 5. Palindromes
n = input()
work = n.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').split(' ')
work = [x for x in work if x]

storage = []

for i in work:
    palindrome = i[::-1]
    if i == palindrome:
        storage.append(i)

storage = list(set(storage))
storage = sorted(storage, key=str.lower) # Sort list of strings lexicographically

print(*storage, sep=', ')
