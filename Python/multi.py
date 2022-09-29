# Date : 29-Sep-2022
# Programmer : MD.Najeeb Uddin



# importing random module from numpy
from numpy import random

# multinomial distribution for a dice
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

# list to store values of dice
values = ['One', 'Two', 'Three', 'Four', 'Five','Six']


# comparing the values with list
for i in range(len(x)):
    if x[0] == i:
        print('Rolling a dice:')
        print(f"it's a {values[i]}")

