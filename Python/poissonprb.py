# Date : 28 - sep - 2022
# Programmer: MD.Najeeb Uddin

# importing numpy module
from numpy import random

frequency = 2
# performing radom poisson

x = random.poisson(lam=frequency, size=10)

print(f"if a person eat {frequency} times a day")
print(f"the probability of the person is as :")

# printing the probabillity
for e in range(len(x)):
    print(f"{x[e]} times on day {e + 1}")
print(x)