from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=1,p=0.5,size=1), hist=True , kde=False)
plt.show()