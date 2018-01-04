# # 1. Exercises: Methods, Debugging and Troubleshooting Code
# # 2. Hello, Name!
# input = input()
#
#
# def print_name(name):
#     print('Hello, {}!'.format(name))
#
#
# print_name(input)

# # 3. Max Method
# nums_a, nums_b, nums_c = int(input()), int(input()), int(input())
#
#
# def get_max(*args):
#     maximum = args[0]
#     for i in args:
#         if i > maximum:
#             maximum = i
#     return maximum
#
#
# result = get_max(nums_a, nums_b, nums_c)
# print(result)

# # 4. English Name оf the Last Digit
# numm = int(input())
# words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#
#
# def last_digit_name(number):
#     character = str(number)[-1]
#     return words[int(character)]
#
#
# result = last_digit_name(numm)
# print(result)

# # 5. Numbers in Reversed Order
# numm = float(input())
#
#
# def reversed_order(number):
#     rev = '{0:g}'.format(number)
#     next = str(rev)[::-1]
#     return float(next)
#
#
# result = reversed_order(numm)
# print('{0:g}'.format(result))

# # 1. Fibonacci Numbers
# n = int(input())
#
#
# def fib(numb):
#     cur = 1
#     old = 1
#     i = 1
#     while i < numb:
#         cur, old, i = cur+old, cur, i+1
#     yield cur
#
#
# for i in fib(n):
#     print(i)

# # 2. Prime Checker
# n = int(input())
#
#
# def is_prime(a):
#     return a > 1 and all(a % i for i in range(2, a))
#
#
# print(is_prime(n))

# # 3. * Primes in Given Range
# class Primes():
#     def __init__(self):
#         self.a, self.b = int(input()), int(input())
#
#     def get_primes(self):
#         lista = []
#         for i in range(self.a, self.b + 1):
#             if i > 1 and all(i % j for j in range(2, i)):
#                 lista.append(i)
#         print(*lista, sep=', ', end='')
#
#
# # Primes().get_primes()       # Just call the class method
# run = Primes()
# run.get_primes()

# # 6. Center Point
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# def print_center(**kwargs):
#     a, b = 0, 0
#     if x1 <= x2:
#         a = x1
#     else:
#         a = x2
#
#     if y1 <= y2:
#         b = y1
#     else:
#         b = y2
#
#     if a != b:
#         print('({0}, {1})'.format(a, b))
#     else:
#         print('({})'.format(a))
#
# print_center(x1 = x1, y1 = y1, x2 = x2, y2 = y2)


# # 8. Cube Properties
# import math
#
# class Cube:
#     def __init__(self):
#         self.side, self.prop = float(input()), input()
#
#     def face_diagonals(self, numb):
#         print('{0:.2f}'.format(math.sqrt(2 * numb ** 2)))
#
#     def space_diagonals(self, numb):
#         print('{0:.2f}'.format(math.sqrt(3 * numb ** 2)))
#
#     def volume(self, numb):
#         print('{0:.2f}'.format(numb ** 3))
#
#     def surface(self, numb):
#         print('{0:.2f}'.format(6 * numb ** 2))
#
#     def dispatch(self):
#         if self.prop == 'face':
#             self.face_diagonals(self.side)
#         elif self.prop == 'space':
#             self.space_diagonals(self.side)
#         elif self.prop == 'volume':
#             self.volume(self.side)
#         elif self.prop == 'surface':
#             self.surface(self.side)
#
#
# Cube().dispatch()

# # 9. Geometry Calculator
# import math
# shape = input()
#
#
# def triangle_area(side, height):
#     print('{0:.2f}'.format(0.5 * (side * height)))
#
#
# def square_are(side):
#     print('{0:.2f}'.format(side ** 2))
#
#
# def rectangle_area(width, height):
#     print('{0:.2f}'.format(width * height))
#
#
# def circle_area(radius):
#     print('{0:.2f}'.format(math.pi * radius ** 2))
#
#
# def dispatch(arg):
#     if arg == 'triangle':
#         a, b = float(input()), float(input())
#         triangle_area(a, b)
#     elif arg == 'square':
#         a = float(input())
#         square_are(a)
#     elif arg == 'rectangle':
#         a, b = float(input()), float(input())
#         rectangle_area(a, b)
#     elif arg == 'circle':
#         a = float(input())
#         circle_area(a)
#
#
# dispatch(shape)

# # 10. Master Numbers
# number = int(input())
#
#
# def is_palindrome(number):
#     if str(number) == str(number)[::-1]:
#         return True
#
#
# def sum_of_digits(number):
#     s = 0
#     while number:
#         s += number % 10
#         number //= 10
#     if s % 7 == 0:
#         return True
#
#
# def contains_even_digit(number):
#     val, boolean = str(number), False
#     for i in val:
#         if int(i) % 2 == 0:
#             boolean = True
#     return boolean
#
#
# def dispatch(arg):
#     for i in range(1, arg + 1):
#         if is_palindrome(i) and sum_of_digits(i) and contains_even_digit(i):
#             print(i)
#
#
# dispatch(number)

# # 11. * Factorial
# number = int(input())
#
#
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(number))

# 12. Factorial Trailing Zeroes
import re
number = int(input())


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def trailing_zeros(numb):
    val = factorial(numb)
    result = re.findall(r'(?<=[1-9])0+$', str(val))[0]
    return int(len(result))


final = trailing_zeros(number)
print(final)
