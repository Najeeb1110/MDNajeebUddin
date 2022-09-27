import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
#loc = mean
#scale = (standarad deviation ) flatness
#size = shape of returned array
x = random.normal(loc=3, scale=6, size =(3,8))
#a is median
a = 0
#sum of observation 
for y in range(len(x)):
    for z in range(len(x[y])):
        a += x[y][z]
#finding the mediam
median = a/len(x)
print(median)
print(x)
sns.distplot(x,hist=True)
plt.show()
