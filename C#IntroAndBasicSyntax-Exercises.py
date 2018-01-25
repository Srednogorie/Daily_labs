# # Problem 1. Debit Card Number
# class DebitCardNumberRepair():
#     number = []
#
#     def debit_card_number(self, partial):
#         result = '{:04}'.format(partial)
#         return result
#
#     def represent(self):
#         print(*self.number, sep=' ')
#
#     def get_input(self):
#         for i in range(4):
#             partial = int(input())
#             done = self.debit_card_number(partial)
#             DebitCardNumberRepair.number.append(done)
#             # self.number.append(done)
#         self.represent()
#
# DebitCardNumberRepair().get_input()

# # Problem 2. Rectangle Area
# class RectangleArea():
#
#     def area(self, a, b):
#         print('{0:.2f}'.format(a * b))
#
#     def get_input(self):
#         a = float(input())
#         b = float(input())
#         self.area(a, b)
#
# RectangleArea().get_input()

# # Problem 3. Miles to Kilometers
# class MilesToKilometers():
#     def __init__(self):
#         self.m_k = 1.60934
#
#     def result(self, distance):
#         print('{0:.2f}'.format(distance * self.m_k))
#
#     def get_input(self):
#         miles = float(input())
#         self.result(miles)
#
# MilesToKilometers().get_input()

# # Problem 4. Beverage Labels
# class BeverageLabels():
#     def __init__(self):
#         self.name = input()
#         self.volume = int(input())
#
#     def represent(self, en, su):
#         print('{0}ml {1}:'.format(self.volume, self.name))
#         print('{0:g}kcal, {1:g}g sugars'.format(en * self.volume, su * self.volume))
#
#     def calculate(self, en_co, su_co):
#         energy = en_co / 100
#         sugar = su_co / 100
#         self.represent(energy, sugar)
#
#     def get_input(self):
#         energy_content = int(input())
#         sugar_content = int(input())
#         self.calculate(energy_content, sugar_content)
#
# BeverageLabels().get_input()

# Problem 5. * Character Stats
class CharacterStats():
    def represent(self, name, c_health, m_health, c_energy, m_energy):
        print('Name: {}'.format(name))
        print('Health: |' + '|' * c_health + '.' * (m_health - c_health) + '|')
        print('Energy: |' + '|' * c_energy + '.' * (m_energy - c_energy) + '|')

    def get_input(self):
        name = input()
        c_health = int(input())
        m_health = int(input())
        c_energy = int(input())
        m_energy = int(input())
        self.represent(name, c_health, m_health, c_energy, m_energy)

CharacterStats().get_input()
