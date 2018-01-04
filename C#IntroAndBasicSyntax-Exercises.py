# # Problem 1. Debit Card Number
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print('{0:04} {1:04} {2:04} {3:04}'.format(a, b, c, d))

# # Problem 2. Rectangle Area
# a, b = float(input()), float(input())
# print('{0:.2f}'.format(a * b))

# # Problem 3. Miles to Kilometers
# miles = float(input())
# print('{0:.2f}'.format(miles * 1.60934))

# # Problem 4. Beverage Labels
# name, volume, energy_content, sugar_content = input(), int(input()), int(input()), int(input())
# energy, sugar = energy_content / 100, sugar_content / 100
# print('{0}ml {1}:'.format(volume, name))
# print('{0:g}kcal, {1:g}g sugars'.format(energy * volume, sugar * volume))

# Problem 5. * Character Stats
name, c_health, m_health, c_energy, m_energy = input(), int(input()), int(input()), int(input()), int(input())
print('Name: {}'.format(name))
print('Health: |' + '|' * c_health + '.' * (m_health - c_health) + '|')
print('Energy: |' + '|' * c_energy + '.' * (m_energy - c_energy) + '|')

