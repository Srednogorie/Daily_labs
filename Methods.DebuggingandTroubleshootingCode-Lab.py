# # 1. Lab: Methods, Debugging and Troubleshooting Code
# # I. Declaring and Invoking Methods
# # 2. Blank Receipt
#
#
# def header():
#     print('CASH RECEIPT')
#     print('------------------------------')
#
#
# def body():
#     print('Charged to____________________')
#     print('Received by___________________')
#
#
# def text():
#     print('------------------------------')
#     print('© SoftUni')
#
#
# def printit():
#     header()
#     body()
#     text()
#
#
# printit()

# # 3. Sign of Integer Number
# n = int(input())
#
#
# def calculate(numb):
#     if numb == 0:
#         print('The number 0 is zero.')
#     elif numb > 0:
#         print('The number {} is positive.'.format(numb))
#     elif numb < 0:
#         print('The number {} is negative.'.format(numb))
#
#
# calculate(n)

# # 4. Printing Triangle
# n = int(input())
#
#
# def print_triangle(numb):
#     for i in range(1, numb + 1):
#         for j in range(i):
#             print(j + 1, end=' ')
#         print()
#     for i in reversed(range(1, numb)):
#         for j in range(i):
#             print(j + 1, end=' ')
#         print()
#
#
# print_triangle(n)

# # 5. Draw a Filled Square
# n = int(input())
#
#
# def header_bottom_row(numb):
#     print('-' * (n * 2))
#
#
# def middle_rows(numb):
#     widht = n * 2
#     cons = int((widht - 2) / 2)
#     for i in range(n - 2):
#         print('-' + '\\/' * cons + '-')
#
#
# header_bottom_row(n)
# middle_rows(n)
# header_bottom_row(n)

# # 6. Temperature Conversion
# n = float(input())
#
#
# def far_cel(numb):
#     return (numb - 32) * (5 / 9)
#
#
# celsius = far_cel(n)
# print('{0:.2f}'.format(celsius))

# # 7. Calculate Triangle Area
# a, b = float(input()), float(input())
#
#
# def triangle_area(a, b):
#     return a * b / 2
#
#
# area = triangle_area(a, b)
#
#
# print('{:g}'.format(area))

# III. Debugging and Program Flow
# 10. Multiply Evens by Odds
n = int(input())


def get_sum_even(numb):
    summ_even = 0
    for i in str(numb):
        if int(i) % 2 == 0:
            summ_even += int(i)
    return summ_even


def get_sum_odd(numb):
    summ_odd = 0
    for i in str(numb):
        if int(i) % 2 == 1:
            summ_odd += int(i)
    return summ_odd

def get_multiplied_even_odd(numb):
    a = get_sum_even(numb)
    b = get_sum_odd(numb)
    return a * b


result = get_multiplied_even_odd(abs(n))
print(result)
